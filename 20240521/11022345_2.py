#動態地圖
#/workspaces/cycu_ai2024/20240521/M05A31_2rows.csv
#/workspaces/cycu_ai2024/20240521/國道計費門架座標及里程牌價表1130327.csv
import pandas as pd

# 讀取csv檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240521/國道計費門架座標及里程牌價表1130327.csv')

# 選擇需要的欄位
df = df[['設定收費區代碼', '緯度', '經度']]
#存下來
df.to_csv('/workspaces/cycu_ai2024/20240521/國道計費門架座標.csv', index=False)