import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
# 讀取csv檔案，並將其轉換為DataFrame
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv', encoding='utf-8')
df['國道名稱'] = df['國道名稱'].fillna('')
# 選取包含"國道1號"的行
df1 = df[df['國道名稱']=='國道1號']
df2 = df1[df1['方向']=='南']
# 印出選取的行
print(df2)
# 設定支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df2['事件開始'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['時'].astype(str) + ':' + df2['分'].astype(str)
df2['事件開始'] = pd.to_datetime(df2['事件開始'])
#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df2['事件排除'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['事件排除'].astype(str)
df2['事件排除'] = pd.to_datetime(df2['事件排除'])
#drop 欄位 '年' '月' '日' '時' '分'
df2 = df2.drop(columns=['年', '月', '日', '時', '分'])
#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
df2['事件開始1'] = df2['事件開始'].apply(lambda x: int(x.timestamp()))
df2['事件排除1'] = df2['事件排除'].apply(lambda x: int(x.timestamp()))
#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df2[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])
# 以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
for index, row in df2.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)
#大標題國道1號南向
plt.title('國道1號南向', fontproperties=font)
#小標題11022345
plt.suptitle('11022345', fontproperties=font)
plt.show()
#-------------------------------------
df1 = df[df['國道名稱']=='國道1號']
df2 = df1[df1['方向']=='北']
# 印出選取的行
print(df2)
# 設定支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df2['事件開始'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['時'].astype(str) + ':' + df2['分'].astype(str)
df2['事件開始'] = pd.to_datetime(df2['事件開始'])
#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df2['事件排除'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['事件排除'].astype(str)
df2['事件排除'] = pd.to_datetime(df2['事件排除'])
#drop 欄位 '年' '月' '日' '時' '分'
df2 = df2.drop(columns=['年', '月', '日', '時', '分'])
#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
df2['事件開始1'] = df2['事件開始'].apply(lambda x: int(x.timestamp()))
df2['事件排除1'] = df2['事件排除'].apply(lambda x: int(x.timestamp()))
#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df2[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])
# 以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
for index, row in df2.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)
#大標題國道1號南向
plt.title('國道1號北向', fontproperties=font)
#小標題11022345
plt.suptitle('11022345', fontproperties=font)
plt.show()
#-------------------------------------
df1 = df[df['國道名稱']=='國道3號']
df2 = df1[df1['方向']=='南']
# 印出選取的行
print(df2)
# 設定支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df2['事件開始'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['時'].astype(str) + ':' + df2['分'].astype(str)
df2['事件開始'] = pd.to_datetime(df2['事件開始'])
#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df2['事件排除'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['事件排除'].astype(str)
df2['事件排除'] = pd.to_datetime(df2['事件排除'])
#drop 欄位 '年' '月' '日' '時' '分'
df2 = df2.drop(columns=['年', '月', '日', '時', '分'])
#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
df2['事件開始1'] = df2['事件開始'].apply(lambda x: int(x.timestamp()))
df2['事件排除1'] = df2['事件排除'].apply(lambda x: int(x.timestamp()))
#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df2[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])
# 以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
for index, row in df2.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)
#大標題國道1號南向
plt.title('國道3號南向', fontproperties=font)
#小標題11022345
plt.suptitle('11022345', fontproperties=font)
plt.show()
#-------------------------------------
df1 = df[df['國道名稱']=='國道3號']
df2 = df1[df1['方向']=='北']
# 印出選取的行
print(df2)
# 設定支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df2['事件開始'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['時'].astype(str) + ':' + df2['分'].astype(str)
df2['事件開始'] = pd.to_datetime(df2['事件開始'])
#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df2['事件排除'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['事件排除'].astype(str)
df2['事件排除'] = pd.to_datetime(df2['事件排除'])
#drop 欄位 '年' '月' '日' '時' '分'
df2 = df2.drop(columns=['年', '月', '日', '時', '分'])
#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
df2['事件開始1'] = df2['事件開始'].apply(lambda x: int(x.timestamp()))
df2['事件排除1'] = df2['事件排除'].apply(lambda x: int(x.timestamp()))
#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df2[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])
# 以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
for index, row in df2.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)
#大標題國道1號南向
plt.title('國道3號北向', fontproperties=font)
#小標題11022345
plt.suptitle('11022345', fontproperties=font)
plt.show()