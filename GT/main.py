import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import lightgbm as lgb
from sklearn.preprocessing import StandardScaler

# --- 1. データ読み込みと前処理 ---
FILENAME = "GT/archive/19860105-20210731_race_result.csv"
try:
    df = pd.read_csv(FILENAME, encoding='utf-8', low_memory=False)
except FileNotFoundError:
    print(f"エラー: ファイル '{FILENAME}' が見つかりません。")
    exit()
print("データの読み込み完了")

df['3着以内フラグ'] = df['着順'].apply(lambda x: 1 if x <= 3 else 0)
df['斤量'] = pd.to_numeric(df['斤量'], errors='coerce')
df['馬体重'] = pd.to_numeric(df['馬体重'], errors='coerce')
df['場体重増減'] = pd.to_numeric(df['場体重増減'], errors='coerce')
df.dropna(subset=['斤量', '馬体重', '場体重増減', '3着以内フラグ'], inplace=True)
print("ターゲット変数の作成完了")

# --- 2. 特徴量エンジニアリング ---
df['レース日付'] = pd.to_datetime(df['レース日付'], errors='coerce')
df.sort_values(by=['馬名', 'レース日付'], inplace=True)
df['前走日付'] = df.groupby('馬名')['レース日付'].transform('shift')
df['レース間隔'] = (df['レース日付'] - df['前走日付']).dt.days
df['レース間隔'].fillna(999, inplace=True)
print("レース間隔の計算完了。")

### --- 特徴量エンジニアリング（馬自身のコース適性）ここから --- ###

print("特徴量エンジニアリング（馬自身のコース適性）を開始...")

# 1. コースを特定するための「コースID」を作成
df['コースID'] = (df['競馬場コード'].astype(str) + "_" +
                df['距離(m)'].astype(str) + "_" +
                df['芝・ダート区分'].astype(str))

# 2. そのレースで好走したかどうかのフラグを作成 (これは元の'3着以内フラグ'と同じ)
#    この後の計算のために、一時的に'好走フラグ'としておく
df['好走フラグ'] = df['3着以内フラグ']

# 3. 馬ごと、コースごとに、過去に何回好走したかを計算する
#    まず馬名と日付でソートされていることを確認
df.sort_values(by=['馬名', 'レース日付'], inplace=True)
#    馬ごと・コースごとにグループ化し、好走フラグを累積和
df['同コース過去好走回数'] = df.groupby(['馬名', 'コースID'])['好走フラグ'].cumsum()

# 4. 「今回のレースを除く」過去の好走回数にするため、自分自身の好走分を引く
df['同コース過去好走回数'] = df['同コース過去好走回数'] - df['好走フラグ']

# 5. 過去の好走回数が1回以上あれば「1」、なければ「0」のフラグを作成
df['コース好走経験'] = df['同コース過去好走回数'].apply(lambda x: 1 if x > 0 else 0)

# 6. 計算に使った一時的な列を削除
df.drop(['コースID', '好走フラグ', '同コース過去好走回数'], axis=1, inplace=True)

print("馬自身のコース適性 計算完了。")

### --- 特徴量エンジニアリング（馬自身のコース適性）ここまで --- ###


# 特徴量として使用する列
features = [
    '枠番', '馬番', '性別', '馬齢', '斤量', '馬体重', '場体重増減',
    'レース間隔',
    'コース好走経験', # ★★★ 新しく追加した特徴量 ★★★
    '競馬場コード', '距離(m)', '芝・ダート区分', '右左回り・直線区分', '天候', '馬場状態1',
    '騎手', '調教師'
]

target = '3着以内フラグ'
# ### ★ 変更点 ★ ###
# この段階で'レースID'も一緒に保持しておく
df_model = df[features + [target, 'レース日付', 'レースID']].copy()

# 騎手と調教師のカテゴリを上位N件に絞る
def limit_categories(series, n=50):
    top_n = series.value_counts().nlargest(n).index
    return series.apply(lambda x: x if x in top_n else 'その他')

df_model['騎手'] = limit_categories(df_model['騎手'], n=50)
df_model['調教師'] = limit_categories(df_model['調教師'], n=50)
print("騎手・調教師のカテゴリを上位50に限定しました。")

# --- 3. 学習データと検証データに分割 ---
SPLIT_DATE = '2021-01-01'
train_df = df_model[df_model['レース日付'] < SPLIT_DATE].copy()
test_df = df_model[df_model['レース日付'] >= SPLIT_DATE].copy()

# 日付列はここで削除
train_df.drop('レース日付', axis=1, inplace=True)
test_df.drop('レース日付', axis=1, inplace=True)

# ターゲットエンコーディング
print("ターゲットエンコーディング（騎手の3着内率）を開始...")
jockey_win_rate = train_df.groupby('騎手')['3着以内フラグ'].mean()
train_df['騎手_3着内率'] = train_df['騎手'].map(jockey_win_rate)
test_df['騎手_3着内率'] = test_df['騎手'].map(jockey_win_rate)
overall_win_rate = train_df['3着以内フラグ'].mean()
train_df['騎手_3着内率'].fillna(overall_win_rate, inplace=True)
test_df['騎手_3着内率'].fillna(overall_win_rate, inplace=True)
train_df.drop('騎手', axis=1, inplace=True)
test_df.drop('騎手', axis=1, inplace=True)
print("ターゲットエンコーディング完了。")
### --- ターゲットエンコーディング（騎手の3着内率）の直後に追加 --- ###

print("特徴量エンジニアリング（騎手と調教師の相性）を開始...")

# 1. '騎手'と'調教師'を結合して「コンビID」を作成
# ※この時点では元の'騎手'列は削除済みなので、df_modelから持ってくる必要がある
#   より安全な方法として、分割前のデータからコンビIDを作成する

# 安全のため、分割前のdf_modelを再度利用してコンビ情報を作成する
train_combi = df_model.loc[train_df.index, ['騎手', '調教師']].copy()
test_combi = df_model.loc[test_df.index, ['騎手', '調教師']].copy()

train_df['コンビID'] = train_combi['騎手'] + "_" + train_combi['調教師']
test_df['コンビID'] = test_combi['騎手'] + "_" + test_combi['調教師']


# 2. 学習データのみを使い、「コンビID」ごとの3着内率を計算
combi_win_rate = train_df.groupby('コンビID')['3着以内フラグ'].mean()

# 3. 計算した率を、学習データと検証データの 'コンビID' 列に紐付け（マッピング）
train_df['コンビ別_3着内率'] = train_df['コンビID'].map(combi_win_rate)
test_df['コンビ別_3着内率'] = test_df['コンビID'].map(combi_win_rate)

# 4. 検証データにしかいないコンビなどで発生した欠損値を、全体の平均値で埋める
#    騎手の3着内率の平均を使うのが妥当
overall_combi_rate = train_df['騎手_3着内率'].mean()
train_df['コンビ別_3着内率'].fillna(overall_combi_rate, inplace=True)
test_df['コンビ別_3着内率'].fillna(overall_combi_rate, inplace=True)

# 5. 元の 'コンビID' 列は不要になったので削除
train_df.drop('コンビID', axis=1, inplace=True)
test_df.drop('コンビID', axis=1, inplace=True)

print("騎手と調教師の相性 計算完了。")

# ワンホットエンコーディング
categorical_features = ['性別', '競馬場コード', '芝・ダート区分', '右左回り・直線区分', '天候', '馬場状態1', '調教師']
train_encoded = pd.get_dummies(train_df, columns=categorical_features, drop_first=True)
test_encoded = pd.get_dummies(test_df, columns=categorical_features, drop_first=True)

# ### ★ 変更点 ★ ###
# AIに学習させる直前で、学習に不要な列をXからドロップする
X_train = train_encoded.drop([target, 'レースID'], axis=1)
y_train = train_encoded[target]
X_test = test_encoded.drop([target, 'レースID'], axis=1)
y_test = test_encoded[target]

# 列の差異を調整
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# --- 4. モデルの学習 ---
print("モデル学習を開始...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = lgb.LGBMClassifier(objective='binary', metric='auc', random_state=42)
model.fit(X_train_scaled, y_train)
print("モデルの学習完了！")

import joblib # ★ ライブラリをインポート

# ( ... model.fit(...) の後 ... )

# 学習済みのモデルとスケーラーをファイルに保存
joblib.dump(model, 'race_predictor_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
# ### ★ 重要 ★ ###
# 学習データの列構成も保存しておく（予測時に必要）
joblib.dump(X_train.columns, 'model_columns.pkl')

print("\nモデルとスケーラーをファイルに保存しました。")


# --- 5. 予測と評価 ---
probabilities = model.predict_proba(X_test_scaled)[:, 1]
threshold = 0.18
y_pred_new = (probabilities >= threshold).astype(int)
precision = precision_score(y_test, y_pred_new)
recall = recall_score(y_test, y_pred_new)
print(f"\n--- しきい値 {threshold} でのモデル評価結果 ---")
print(f"適合率 (Precision): {precision:.4f}")
print(f"再現率 (Recall): {recall:.4f}")
print("---------------------------------")

# --- 6. 予測結果の整形 ---
# ### ★ 変更点 ★ ###
# test_encodedに既に正しい情報があるので、それを使う
results_df = test_encoded[['レースID', '馬番']].copy()
results_df['確率'] = probabilities

### --- 7. バックテスト機能 (期待値ベッティング版 + 詳細レポート) --- ###

print("\n\n--- バックテスト実行 (期待値ベッティング戦略) ---")

# (オッズデータの読み込み部分は同じ)
ODDS_FILENAME = "GT/archive/19860105-20210731_odds.csv"
try:
    odds_df = pd.read_csv(ODDS_FILENAME, encoding='utf-8', low_memory=False)
except FileNotFoundError:
    print(f"エラー: オッズファイル '{ODDS_FILENAME}' が見つかりません。")
    exit()

# (複勝データの前処理部分は同じ)
fukusho_payouts = {}
for i in range(1, 6):
    df_temp = odds_df[['レースID', f'複勝{i}_馬番', f'複勝{i}_オッズ']].copy()
    df_temp.rename(columns={f'複勝{i}_馬番': '馬番', f'複勝{i}_オッズ': '複勝払戻'}, inplace=True)
    for index, row in df_temp.iterrows():
        if pd.notna(row['馬番']):
            race_id, baban, payout = row['レースID'], int(row['馬番']), row['複勝払戻']
            if race_id not in fukusho_payouts: fukusho_payouts[race_id] = {}
            fukusho_payouts[race_id][baban] = payout

# --- ★ カウンターの初期化 ★ ---
total_investment = 0
total_return = 0
bet_count = 0  # 実際に賭けた回数（馬の数）
races_betted = set() # 賭けたレースのIDを保存するセット
total_races_in_test = results_df['レースID'].nunique() # 検証セットの全レース数

# AIの予測結果と複勝データを結合
backtest_df = test_df[['レースID', '馬番']].copy()
backtest_df['確率'] = probabilities

# シミュレーションループ
for index, row in backtest_df.iterrows():
    race_id, baban, prob = row['レースID'], int(row['馬番']), row['確率']
    
    race_odds_info = odds_df[odds_df['レースID'] == race_id]
    if race_odds_info.empty or pd.isna(race_odds_info.iloc[0]['複勝1_オッズ']):
        continue
    
    fukusho_odds = race_odds_info.iloc[0]['複勝1_オッズ'] / 100.0
    expected_value = prob * fukusho_odds
    
    if expected_value > 1.0:
        # --- ★ カウンターを更新 ★ ---
        total_investment += 100
        bet_count += 1
        races_betted.add(race_id)
        
        if race_id in fukusho_payouts and baban in fukusho_payouts[race_id]:
            payout = fukusho_payouts[race_id][baban]
            total_return += payout

# --- ★ 最終結果の表示（詳細レポート付き）★ ---
print("\n--- バックテスト最終結果 (期待値ベッティング) ---")
print(f"検証対象の全レース数: {total_races_in_test} レース")
print(f"賭けたレース数: {len(races_betted)} レース")
print(f"見送ったレース数: {total_races_in_test - len(races_betted)} レース")
print("-" * 25)
print(f"総投資回数（賭けた馬の数）: {bet_count} 回")
print(f"総投資額: {total_investment} 円")
print(f"総回収額: {total_return:,.0f} 円")

if total_investment > 0:
    roi = (total_return / total_investment) * 100
    print(f"回収率: {roi:.2f} %")
else:
    print("投資対象レースがありませんでした。")

