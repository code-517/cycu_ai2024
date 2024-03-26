#https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/
#TDCS_M04A_20240325_000000.csv
#TDCS_M04A_20240325_005500.csv
#/workspaces/cycu_ai2024/20240326
import requests
from bs4 import BeautifulSoup
import os

# 檔案名稱的基本部分
base_file_name = 'TDCS_M04A_20240325_'
for h in range(24):
    #base_url變成https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/01/
    if h < 10:
        base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/0' + str(h) + '/'
    else:
        base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/' + str(h) + '/'

    for i in range(0, 5501, 500):
        # 生成檔案名稱
        file_name = base_file_name + str(h).zfill(2) + str(i).zfill(4) + '.csv'

        # 檔案的完整 URL
        file_url = base_url + file_name

        # 發送 GET 請求來下載檔案
        response = requests.get(file_url)

        # 將檔案寫入到指定的資料夾
        with open('/workspaces/cycu_ai2024/20240326/' + file_name, 'wb') as file:
            file.write(response.content)