#/workspaces/cycu_ai2024/20240430/combinedM05A.csv
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/combinedM05A.csv')

# 選擇第4個欄位（假設欄位名稱為 'Column4'）為 31 的那一列
selected_rows = df[(df['gate'].str.startswith('01')) & (df['Value1'] == 31)]
# 將選定的列寫入到一個新的 CSV 檔案中
selected_rows.to_csv('/workspaces/cycu_ai2024/20240430/M05AS31_rows.csv', index=False)