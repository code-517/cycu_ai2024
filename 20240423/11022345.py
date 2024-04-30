#https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/
#TDCS_M04A_20240325_000000.csv
#TDCS_M04A_20240325_005500.csv
#/workspaces/cycu_ai2024/20240326
import requests
from bs4 import BeautifulSoup
import os
from datetime import timedelta, date

# 定義一個函數來生成日期範圍
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2024, 4, 15)
end_date = date(2024, 4, 22)

for single_date in daterange(start_date, end_date):
    for h in range(24):
        if h < 10:
            base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/' + single_date.strftime("%Y%m%d") + '/0' + str(h) + '/'
        else:
            base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/' + single_date.strftime("%Y%m%d") + '/' + str(h) + '/'

        for i in range(0, 5501, 500):
            file_name = 'TDCS_M05A_' + single_date.strftime("%Y%m%d") + '_' + str(h).zfill(2) + str(i).zfill(4) + '.csv'
            file_url = base_url + file_name

            response = requests.get(file_url)

            if response.status_code == 200:
                with open('/workspaces/cycu_ai2024/20240423/' + file_name, 'wb') as file:
                    file.write(response.content)
            else:
                print('Failed to download file: ' + file_url)