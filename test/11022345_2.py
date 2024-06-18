#D:\github\1\cycu_ai2024\Exam\test\113年中華民國政府行政機關辦公日曆表.csv
# 找到指定路徑中的所有 CSV 檔案
import pandas as pd
import glob
from datetime import datetime

#D:\github\1\cycu_ai2024\Exam\test_M05A\M05A

# 設定包含所有 CSV 檔案的資料夾路徑
base_path = 'D:/github/1/cycu_ai2024/Exam/test_M05A/M05A'

# 使用 glob.glob() 來找到所有 CSV 檔案，包括子資料夾內的檔案
csv_files = glob.glob(f'{base_path}/**/**/*.csv', recursive=True)
# 讀取並合併所有的 CSV 檔案
df = pd.concat([pd.read_csv(f) for f in csv_files])

# 指定欄位名稱
df.columns = ['TimeStamp', 'GantryFrom', 'GantryTo', 'VehicleType', 'Speed', 'Volume']

# 篩選出 'GantryFrom' 列中值為 '01F0584N'、'01F0633N'、'01F0578S' 或 '01F0633S' 的行
df = df[df['GantryFrom'].isin(['01F0584N', '01F0633N', '01F0578S', '01F0633S'])]
df = df[df['VehicleType'] == 31]
# 假設您的 DataFrame 有一個名為 'TimeStamp' 的列，其中包含日期信息
# 如果不是，請將 'TimeStamp' 替換為實際的列名
for date, group in df.groupby(df['TimeStamp'].dt.date):
    # 將日期轉換為指定的格式
    date_str = date.strftime('%Y%m%d')

    # 儲存每一天的數據為一個新的 CSV 檔案
    group.to_csv(f'D:\\github\\1\\cycu_ai2024\\Exam\\test_M05AC\\M05A_{date_str}.csv', index=False)