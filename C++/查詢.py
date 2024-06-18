#讀取、寫入檔案
#r讀取
#w覆寫
#a在原先資料後再寫東西
import json
# json 是一種資料型態
# 會引用json裡面有些函式能夠讓字典變成字串等等
def getwrite():
    with open('chart.json','r') as f:
        return json.loads(f.read())
    #以r模式開啟chart檔案後
    #loads()是把從chart檔案讀取到的json格式字串轉換python資料的格式
    #此函式的用途是獲得chart.json 裡面資料並且回傳
def checkname(name):
    get=getwrite()
    #get等於資料裡面的東西
    if name in get.keys():
        return False
    else:
        return True
    #此函式的作用就是檢查資料裡面有沒有已經存在過這個城市的資料了
    #有就傳送False
    #沒有就傳送True
    #為什麼有是傳送False，是因為之後用途如果記錄到同一個城市的話會把之前的紀錄的刷掉
def read(name):
    if checkname(name):
         print('沒有此城市紀錄')
    else:
        get=getwrite()
        waterneed = get[name]['waterneed']
        print(name,'水庫需水量:',waterneed,'ft^2')
    #此函式作用就是先呼叫有checkname函式檢查有沒有
    #有的話在讀取出資料
    
