import pandas as pd
import math

# --- 設定項目 ---
# 元の巨大なCSVファイルの名前
input_filename = 'GT/archive/19860105-20210731_race_result.csv'
# 新しく作成するファイルの名前
output_filename = 'your_smaller_file_head.csv'
# ----------------

# 1. 元ファイルの総行数を調べる（メモリをあまり使わない方法）
total_rows = sum(1 for row in open(input_filename, 'r')) - 1 # ヘッダー分を引く

# 2. 抽出する行数（全体の1/3）を計算
rows_to_keep = math.ceil(total_rows / 100)

# 3. 指定した行数だけファイルを読み込む
df_small = pd.read_csv(input_filename, nrows=rows_to_keep)

# 4. 新しいファイルとして保存
df_small.to_csv(output_filename, index=False)

print(f"'{output_filename}' の作成が完了しました。")