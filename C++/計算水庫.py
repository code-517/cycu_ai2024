def average(ave):
    #月流入量 monthin
    monthin=[]
    for i in range(1,13,1):
        for j in range (1,13,2):
            if i==j and i!=9 and i!=11 or i==8 or i==10 or i==12:
                go=round(ave[i-1]*86400*31/100000,2)
                monthin.append(go)
                break
            elif i==2:
                go=round(ave[i-1]*86400*28/100000,2)
                monthin.append(go)
                break
            else:
                if i<=j:
                    go=round(ave[i-1]*86400*30/100000,2)
                    monthin.append(go)
                    break
    #透過雙迴圈，做到檢查月份像是1月而後算式就後面乘30天的同時在運算從1月-12月的所有月流入量
    #用round()取小數點第2點
    return monthin

def out(wout):
    #蒸發流出量 out
    out=[]
    for i in range(1,13,1):
        for j in range (1,13,2):
            if i==j and i!=9 and i!=11 or i==8 or i==10 or i==12:
                go=round(wout*31/100000,2)
                out.append(go)
                break
            elif i==2:
                go=round(wout*28/100000,2)
                out.append(go)
                break
            else:
                if i<=j:
                    go=round(wout*30/100000,2)
                    out.append(go)
                    break
    #透過雙迴圈，做到檢查月份像是1月而後算式就後面乘30天的同時在運算從1月-12月的所有蒸發流出量
    #用round()取小數點第2點
    return out

def monthneed(people,gal):
    #月需水量 need
    need=[]
    for i in range(1,13,1):
        for j in range (1,13,2):
            if i==j  and i!=9 and i!=11 or i==8 or i==10 or i==12:
                go=round(people*gal*0.134*31/100000,2)
                need.append(go)
                break
            elif i==2:
                go=round(people*gal*0.134*28/100000,2)
                need.append(go)
                break
            else:
                if i<=j: 
                    go=round(people*gal*0.134*30/100000,2)
                    need.append(go)
                    break
    #透過雙迴圈，做到檢查月份像是1月而後算式就後面乘30天的同時在運算從1月-12月的所有月需水量
    #用round()取小數點第2點
    return need

def mingo(minn):
    #最小流出量 minout
    minout=[]
    for i in range(1,13,1):
        for j in range (1,13,2):
            if i==j  and i!=9 and i!=11 or i==8 or i==10 or i==12:
                go=round(minn*86400*31/100000,2)
                minout.append(go)
                break
            elif i==2:
                go=round(minn*86400*28/100000,2)
                minout.append(go)
                break
            else:
                if i<=j:
                    go=round(minn*86400*30/100000,2)
                    minout.append(go)
                    break
    #透過雙迴圈，做到檢查月份像是1月而後算式就後面乘30天的同時在運算從1月-12月的所有最小流出量
    #用round()取小數點第2點
    return minout

def calculate(monthin,wout,need,minout):
    go=0
    ans=0
    for i in range(0,12,1):
        go=monthin[i]-(wout[i]+need[i]+minout[i])
        if go<0:
            ans+=go
    return round(ans,2)
    #把12個月份的收支平衡後，把負的累加起來後就是水庫最少需要
    #用round()取小數點第2點
