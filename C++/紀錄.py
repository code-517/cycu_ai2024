#讀取、寫入檔案
#r讀取
#w覆寫
#a在原先資料後再寫東西
import json
# json 是一種資料型態
# 會引用json裡面有些函式能夠讓字典變成字串等等
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
def getwrite():
    with open('chart.json','r') as f:
        return json.loads(f.read())
    #以r模式開啟chart檔案後
    #loads()是把從chart檔案讀取到的json格式字串轉換python資料的格式
    #此函式的用途是獲得chart.json 裡面資料並且回傳
def addwrite(name,waterneed):
    if checkname(name):
        get=getwrite()
        #get等於資料裡面的東西
        get[name]={'waterneed':waterneed}
        with open('chart.json','w') as f:
            f.write(json.dumps(get))
            #dump()把get字典轉成字串
            #write()把get裡面的字典寫進去chart.json
        print('輸入成功')
    else:
        print('輸入失敗')
