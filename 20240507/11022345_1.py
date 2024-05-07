#/workspaces/cycu_ai2024/20240430/ALL.csv
#讀取csv檔
import pandas as pd
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/ALL.csv')
#把5-8的欄位都刪掉並輸出一個新的csv檔
df = df.drop(df.columns[4:8], axis=1)
df.to_csv('/workspaces/cycu_ai2024/20240507/11022345_1.csv', index=False)
#ploply