import pandas as pd
#M05AS31_rows
# 讀取 CSV 檔案
# 讀取第一個 CSV 檔案
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/NEWcombinedM03A.csv')
print("Successfully read the first CSV file.")
# 讀取第二個 CSV 檔案
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/M05AS31_rows.csv')
print("Successfully read the second CSV file.")
df1['time'] = pd.to_datetime(df1['time'], format='%Y-%m-%d %H:%M')
df2['Time'] = pd.to_datetime(df2['Time'], format='%Y/%m/%d %H:%M')
print("df1:")
print(df1.head())
print("\ndf2:")
print(df2[['Time','gate', 'Value2']].head())
# 將 df1 和 df2 進行合併，並只保留 'Value2' 欄位
# 將 df1 和 df2 進行合併，並只保留 'Value2' 欄位
df1 = pd.merge(df1, df2[['Time','gate', 'Value2']], how='left', left_on=['time', 'gate'], right_on=['Time', 'gate'])
df1 = df1.drop(columns=['Time'])
df1 = df1.rename(columns={'Value2': '31小客車速度'})
df1.to_csv('/workspaces/cycu_ai2024/20240430/ALL.csv', index=False)