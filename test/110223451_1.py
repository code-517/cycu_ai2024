import requests
import tarfile
import os
from datetime import timedelta, date
from datetime import datetime

start_date = datetime.strptime('2024-04-01', '%Y-%m-%d')
end_date = datetime.strptime('2024-04-30', '%Y-%m-%d')
directory = 'D/workspaces/cycu_ai2024/test/test_M05A'  # 請將此路徑更改為您希望存儲下載文件的目錄

current_date = start_date
while current_date <= end_date:
    base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/'
    tar_gz_url = base_url + 'M05A_' + current_date.strftime("%Y%m%d") + '.tar.gz'
    response = requests.head(tar_gz_url)
    if response.status_code == 200:
        try:
            response = requests.get(tar_gz_url, stream=True)
            with tarfile.open(fileobj=response.raw, mode="r|gz") as file:
                file.extractall(path=directory)
            print(f'Successfully downloaded and extracted {tar_gz_url}')
        except Exception as e:
            print(f'Failed to download and extract {tar_gz_url}. Error: {e}')
    # ...
    else:
        print(f'{tar_gz_url} does not exist.')
        for h in range(24):
            hour_url = base_url + current_date.strftime("%Y%m%d") + '/' + str(h).zfill(2) + '/'
            for i in range(0, 5501, 500):
                file_name = 'TDCS_M05A_' + current_date.strftime("%Y%m%d") + '_' + str(h).zfill(2) + str(i).zfill(4) + '.csv'
                file_url = hour_url + file_name
                response = requests.head(file_url)
                if response.status_code == 200:
                    try:
                        response = requests.get(file_url)
                        with open(directory + '\\' + file_name, 'wb') as file:
                            file.write(response.content)
                        print(f'Successfully downloaded {file_url}')
    # ...
                    except Exception as e:
                        print(f'Failed to download {file_url}. Error: {e}')
                else:
                    print(f'{file_url} does not exist.')
    current_date += timedelta(days=1)