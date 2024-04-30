from datetime import timedelta, date
import os
import pandas as pd

# 定義一個函數來生成日期範圍
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# 檔案路徑
folder_path = '/workspaces/cycu_ai2024/'

# 定義欄位名稱
column_names = ['Time', 'gate', 'gate1', 'Value1', 'Value2', 'Value3']

# 儲存所有 DataFrame 的列表
dfs = []

start_date = date(2024, 4, 29)
end_date = date(2024, 4, 30)

for single_date in daterange(start_date, end_date):
    # 檔案名稱的基本部分
    base_file_name = 'TDCS_M05A_' + single_date.strftime("%Y%m%d") + '_'

    # 迴圈遍歷每個小時
    for h in range(24):
        # 迴圈遍歷每個 500 秒
        for i in range(0, 5501, 500):
            # 生成檔案名稱
            file_name = base_file_name + str(h).zfill(2) + str(i).zfill(4) + '.csv'
            # 檔案的完整路徑
            file_path = os.path.join(folder_path, file_name)
            # 讀取 CSV 檔案並將其添加到列表中
            if os.path.exists(file_path):
                df = pd.read_csv(file_path, names=column_names)
                dfs.append(df)

# 合併所有的 DataFrame
df_combined = pd.concat(dfs, ignore_index=True)

# 將合併後的 DataFrame 存為 CSV 檔案
df_combined.to_csv('/workspaces/cycu_ai2024/20240430/combinedM05A.csv', index=False)
print(df_combined)