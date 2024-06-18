#月流入量 monthin
#蒸發流出量 wout
#月需水量 need
#最小流出量 minout
import 計算水庫
import 紀錄
import 查詢
ave=[]
while True:
    enter=input('請輸入你要的模式(a查詢b運算)')
    if enter=='a':
        name=input('請輸入城市名稱')
        查詢.read(name)
    #開啟查詢.py用裡面read函式功能獲取記錄在別處的資料
    if enter=='b':
        break
    #查詢完的話就直接進入運算環節
name=input('請輸入城市名稱')       
for i in range(1,13,1):
    print('請輸入',i,'月平均流量')
    append=eval(input())
    ave.append(append)
#進入迴圈讓使用者重複輸入而後把12個月份的平均流量依序存入串列
people=eval(input('請輸入都市人口'))
gal=eval(input('請輸入設計河川自來水的日用量(單位gal)'))
minn=eval(input('請輸入水壩下端河川需保持最小流量為多少(單位cfs)'))
wout=eval(input('當地蒸發量為多少(單位ft^2/day)'))
          
monthin=計算水庫.average(ave)
#月流入量 monthin 使用了計算水庫的average函式來算答案
wout=計算水庫.out(wout)
#蒸發流出量 wout 使用了計算水庫的out函式來算答案
need=計算水庫.monthneed(people,gal)
#月需水量 need 使用了計算水庫的monthneed函式來算答案
minout=計算水庫.mingo(minn)
#最小流出量 minout 使用了計算水庫的mingo函式來算答案
print('月',end='\t')
print('月流入量',end='\t')
print('蒸發流出量',end='\t')
print('月需水量',end='\t')
print('最小流出量(10^5)')
for i in range(1,13,1):
    print(str(i),end='\t')
    print(str(monthin[i-1]),end='\t\t')
    print(str(wout[i-1]),end='\t\t')
    print(str(need[i-1]),end='\t\t')
    print(str(minout[i-1]))
#把12個月份列印出表格
waterneed=計算水庫.calculate(monthin,wout,need,minout)
#利用計算水庫calculate函式計算出答案
print('水庫最少需要',waterneed,'*10^5  (ft^2)')
#轉換一個名稱 方便之後讀懂

ao=input('請問是否新增此次資料(yes or no)')
if ao=='yes':
    紀錄.addwrite(name,waterneed)
    #呼叫紀錄裡面的addwrite函式把資料寫進去檔案
else:
    print('謝謝你的使用')

