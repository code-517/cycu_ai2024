#/workspaces/cycu_ai2024/20240430/combinedM05A.csv
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/combinedM05A.csv')
selected_rows = df[(df['gate'].str.startswith('01')) & (df['Value1'] == 31)]
# 更改欄位名稱
selected_rows= selected_rows.rename(columns={
    'Time': 'Time',
    'gate': 'GantryFrom',
    'gate1': 'GantryTo',
    'Value1': '車種小客車',
    'Value2': 'SpaceMeanSpeed',
    'Value3': 'Traffic'
})

# 將更改後的 DataFrame 寫入到一個新的 CSV 檔案中
selected_rows.to_csv('/workspaces/cycu_ai2024/20240521/M05A31_2rows.csv', index=False)