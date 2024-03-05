#https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table')

dataframes = []
for table in tables:
    data = []
    headers = [header.text.replace('\n', '') for header in table.find('tr').find_all('th')]
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.replace('\n', '') for cell in cells]
        data.append(cells)
    df = pd.DataFrame(data, columns=headers)
    dataframes.append(df)
# Check if dataframes is not empty before accessing its elements
#print(dataframes[1])
#把dataframes[1]資料存成csv檔
#dataframes[1].to_csv('11022345_oil.csv', index=False, encoding='utf-8-sig')
#dataframes[1]只保留前五欄
dataframes[1] = dataframes[1].iloc[:, :5]
#print(dataframes[1])
urk2= "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx"
response2 = requests.get(urk2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
tables2 = soup2.find_all('table')
dataframes2 = []
for table in tables2:
    data2 = []
    headers2 = [header.text.replace('\n', '') for header in table.find('tr').find_all('th')]
    for row in table.find_all('tr')[1:]:
        cells2 = row.find_all('td')
        cells2 = [cell.text.replace('\n', '') for cell in cells2]
        data2.append(cells2)
    df2 = pd.DataFrame(data2, columns=headers2)
    dataframes2.append(df2)
#print(dataframes2[1])
#幫我留下前五欄
dataframes2[1] = dataframes2[1].iloc[:, :5]
#print(dataframes2[1])
#幫我兩個dataframes上下合併
df_all = pd.concat([dataframes[1], dataframes2[1]], axis=0)
#print(df_all)
#把df_all存成csv檔
#df_all.to_csv('11022345_oil1999-2024.csv', index=False, encoding='utf-8-sig')

#matplotlib畫圖
# 把date欄位的資料型態改成日期
products = ['無鉛汽油92', '無鉛汽油95', '無鉛汽油98', '超級/高級柴油']
df_all['調價日期'] = df_all['調價日期'].fillna(method='ffill')
for product in products:
    df_all[product] = df_all[product].fillna(method='ffill')
    df_all[product] = df_all[product].fillna(method='bfill')
    df_all[product] = pd.to_numeric(df_all[product], errors='coerce')
    df_all[product].interpolate(method='linear', inplace=True)
myfont = FontProperties(fname=r'C:\Windows\Fonts\msjh.ttc')

# 畫出折線圖
plt.figure(figsize=(10, 6))
for product in products:
    plt.plot(df_all['調價日期'], df_all[product], label=product)
plt.xlabel('年份', fontproperties=myfont)
plt.ylabel('價格', fontproperties=myfont)
plt.title('1999-2024年油價走勢', fontproperties=myfont)
plt.legend(prop=myfont)
plt.show()
