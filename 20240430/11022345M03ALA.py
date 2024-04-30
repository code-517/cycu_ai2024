#/workspaces/cycu_ai2024/20240430/combinedM03A.csv
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/combinedM03A.csv')
# 將 'Value1' 欄位轉換為字串，以便將其用作新的欄位名稱
df['Value1'] = df['Value1'].astype(str)

# 使用 pivot_table() 函數將 'Value1' 欄位的值轉換為新的欄位
pivot_df = df.pivot_table(index=['Time', 'gate', 'direct'], columns='Value1', values='Value2', fill_value=0)

# 將索引重設為欄位
pivot_df.reset_index(inplace=True)

# 更改欄位名稱
pivot_df.columns = ['time', 'gate', 'direct', '31小客車', '32小貨車', '41大客車', '42大貨車', '5聯結車']

# 將所有浮點數欄位轉換為整數
for col in ['31小客車', '32小貨車', '41大客車', '42大貨車', '5聯結車']:
    pivot_df[col] = pivot_df[col].astype(int)

# 選擇 'gate' 欄位的值以 '01' 開頭的行
pivot_df = pivot_df[pivot_df['gate'].str.startswith('01')]

# 將處理後的 DataFrame 寫入到一個新的 CSV 檔案中
pivot_df.to_csv('/workspaces/cycu_ai2024/20240430/NEWcombinedM03A.csv', index=False)