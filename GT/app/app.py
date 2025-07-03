import streamlit as st
import pandas as pd
import joblib
import os # ★ osライブラリをインポート

# --- AIモデルと関連ファイルの読み込み（絶対パス指定版）---

# このapp.pyファイル自身の場所を基準にする
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# 基準の場所とファイル名を結合して、ファイルの絶対的な住所（絶対パス）を作成
MODEL_PATH = os.path.join(APP_DIR, 'race_predictor_model.pkl')
SCALER_PATH = os.path.join(APP_DIR, 'scaler.pkl')
COLUMNS_PATH = os.path.join(APP_DIR, 'model_columns.pkl')

try:
    # 絶対パスを使ってファイルを読み込む
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    model_columns = joblib.load(COLUMNS_PATH)
except FileNotFoundError as e:
    st.error(f"モデルファイルが見つかりません。以下のパスにファイルが存在するか確認してください。")
    st.error(e) # 詳細なエラーパスを表示
    st.stop()

# --- Webアプリのタイトルと説明 ---
st.title("🏇 AI競馬予測")
st.write("レースに出走する馬の情報を入力すると、3着以内に入る確率を予測します。")

# ( ... これ以降のコードは全く同じです ... )

# --- ユーザー入力画面の作成 ---
st.header("馬の情報を入力")

# 2列レイアウト
col1, col2 = st.columns(2)

with col1:
    baban = st.number_input('馬番', min_value=1, max_value=18, value=1)
    wakuban = st.number_input('枠番', min_value=1, max_value=8, value=1)
    kinryo = st.number_input('斤量', min_value=48.0, max_value=60.0, value=55.0, step=0.5)
    barei = st.number_input('馬齢', min_value=2, max_value=10, value=3)

with col2:
    race_interval = st.number_input('レース間隔（日）', min_value=0, value=28)
    bataiju = st.number_input('馬体重', min_value=400, max_value=600, value=480)
    zogen = st.number_input('馬体重増減', min_value=-30, max_value=30, value=0)
    sex = st.selectbox('性別', ['牡', '牝', 'せん'])

# --- 予測ボタン ---
if st.button('予測する'):
    # --- 入力データの前処理 ---
    
    # 1. 入力データをDataFrameに変換
    input_data = {
        '枠番': [wakuban],
        '馬番': [baban],
        '性別': [sex],
        '馬齢': [barei],
        '斤量': [kinryo],
        '馬体重': [bataiju],
        '場体重増減': [zogen],
        'レース間隔': [race_interval],
        # ここでは固定値やダミーの値を入れる（本来はこれも入力させる）
        '競馬場コード': [1], # ダミー
        '距離(m)': [1600], # ダミー
        '芝・ダート区分': [1], # ダミー
        '右左回り・直線区分': [1], # ダミー
        '天候': ['晴'], # ダミー
        '馬場状態1': ['良'], # ダミー
        '調教師': ['その他'], # ダミー
        '騎手_3着内率': [0.2], # ダミー（本来は騎手名から計算）
        'コンビ別_3着内率': [0.2], # ダミー
        'コース好走経験': [0] # ダミー
    }
    input_df = pd.DataFrame(input_data)
    
    # 2. カテゴリ変数をワンホットエンコーディング
    input_encoded = pd.get_dummies(input_df)
    
    # 3. 学習時の列構成に合わせる
    input_reindexed = input_encoded.reindex(columns=model_columns, fill_value=0)
    
    # 4. データをスケーリング
    input_scaled = scaler.transform(input_reindexed)

    # --- AIによる予測 ---
    prediction_proba = model.predict_proba(input_scaled)[:, 1]

    # --- 結果の表示 ---
    st.header("予測結果")
    st.success(f"この馬が3着以内に入る確率は **{prediction_proba[0]:.2%}** です。")