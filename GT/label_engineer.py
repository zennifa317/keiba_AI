import pandas as pd

def label_engineer(df):

    # 着順が3位以内なら1、それ以外は0
    df['within_3rd_place'] = df['着順'].apply(lambda x: 1 if x <= 3 else 0)

    # OHE騎手名
    columns_to_drop = ['レース日付', '開催回数', '競馬場名', '開催日数', '馬体重', '着順']
    df = df.drop(columns=columns_to_drop)
    print(df.head())
    
    return df

