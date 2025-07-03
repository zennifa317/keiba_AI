# データの時間範囲を確認するコードを追加
import pandas as pd
df = pd.read_csv("GT/archive/19860105-20210731_race_result.csv", encoding='utf-8', low_memory=False) 

df['レース日付'] = pd.to_datetime(df['レース日付']) # 日付形式に変換
print(f"データの日付範囲: {df['レース日付'].min()} から {df['レース日付'].max()} まで")