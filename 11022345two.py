#幫我把剛剛載下來的CSV合併成一個檔案
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 檔案路徑
folder_path = '/workspaces/cycu_ai2024/20240326/'

# 檔案名稱的基本部分
base_file_name = 'TDCS_M04A_20240325_'

# 定義欄位名稱
column_names = ['Time', 'Start', 'End', 'Value1', 'Value2', 'Value3']

# 儲存所有 DataFrame 的列表
dfs = []

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
df_combined.to_csv('/workspaces/cycu_ai2024/20240326/combined.csv', index=False)
print(df_combined)