import requests
from bs4 import BeautifulSoup
import os
from datetime import timedelta, date
import tarfile

#C:\Users\User\Desktop\1\cycu_ai2024\20240521
# 定義一個函數來生成日期範圍
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date1 = date(2024, 1, 1)
end_date1 = date(2024, 3, 28)

start_date2 = date(2024, 3, 29)
end_date2 = date(2024, 4, 30)




# 其他程式碼保持不變...

# 確保目錄存在
directory = r'C:\Users\User\Desktop\1\cycu_ai2024\20240521'
if not os.path.exists(directory):
    os.makedirs(directory)

for single_date in daterange(start_date1, end_date1):
    file_name = 'M05A_' + single_date.strftime("%Y%m%d") + '.tar.gz'
    base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/'
    file_url = base_url + file_name

    response = requests.get(file_url)

    try:
        # 下載和解壓縮檔案的程式碼...
    
        if response.status_code == 200:
            with open(directory + '\\' + file_name, 'wb') as file:
                file.write(response.content)
    
            print('Downloaded file: ' + file_url)
    
            # 解壓縮.tar.gz檔案
            tar = tarfile.open(directory + '\\' + file_name)
            tar.extractall(path=directory)
            tar.close()
    
            print('Extracted file: ' + file_name)
    
        else:
            print('Failed to download file: ' + file_url)
    
    except Exception as e:
        print('An error occurred: ' + str(e))
# 其他程式碼保持不變...

# 其他程式碼保持不變...

for single_date in daterange(start_date2, end_date2):
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
                with open(directory + '\\' + file_name, 'wb') as file:
                    file.write(response.content)
            else:
                print('Failed to download file: ' + file_url)