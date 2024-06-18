import yfinance as yf
import mplfinance as mpf
from matplotlib import rcParams
import pandas as pd
import requests

def paint(df, macd, signal, hist, upper_band, middle_band, lower_band, stock_code):
    import mplfinance as mpf  # 確保導入mplfinance

    # 創建MACD、信號線、柱狀體和布林通道的圖表
    apds = [mpf.make_addplot(macd, panel=1, color='fuchsia', title='MACD'),
        mpf.make_addplot(signal, panel=1, color='b'),
        mpf.make_addplot(hist, panel=1, type='bar', color='dimgray'),
        mpf.make_addplot(upper_band, color='r'),  # 布林上線
        mpf.make_addplot(middle_band, color='g'),  # 布林中線
        mpf.make_addplot(lower_band, color='r')]  # 布林下線

    # 繪製圖表
    mpf.plot(df, type='candle', style='charles',
         title=f'{stock_code} 股票K線圖',
         ylabel='價格（TWD）',
         addplot=apds,
         figscale=1.5,  # 調整圖表大小
         savefig=f'/workspaces/cycu_ai2024/20240618/stock/{stock_code}.png')
# 獲取台灣證券交易所所有股票代碼
res = requests.get('https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL')
df = pd.DataFrame(res.json())
# 只要第一列欄位
stock_codes = df.iloc[:, 0]
# 每個都加上.TW後做成list
stock_codes = stock_codes + '.TW'

# 設定中文字體
rcParams['font.family'] = 'Noto Sans CJK JP'

for stock_code in stock_codes:
    try:
        # 使用yfinance獲取特定股票的數據
        df = yf.download(stock_code, start='2024-01-01', end='2024-6-19')

        if len(df) == 0:
            print(f"{stock_code} 沒有數據.")
            continue

        # 計算MACD
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        hist = macd - signal  # 計算柱狀體

        macd_mean = macd.rolling(window=20).mean()
        macd_std = macd.rolling(window=20).std()
        macd_z_score = (macd - macd_mean) / macd_std

        # 計算布林通道
        middle_band = df['Close'].rolling(window=20).mean()
        std_dev = df['Close'].rolling(window=20).std()
        upper_band = middle_band + (std_dev * 2)
        lower_band = middle_band - (std_dev * 2)

        # 檢查最後一天的收盤價相對於布林通道的位置，
        # 檢查DataFrame是否為空
        if not df.empty and df['Volume'].tail(10).mean() > 100000 and df['Close'].iloc[-1] > 50 :
            # 檢查最後一天的收盤價與布林通道和MACD Z-score的關係
            close_last = df['Close'].iloc[-1]
            upper_last = upper_band.iloc[-1]
            lower_last = lower_band.iloc[-1]
            macd_z_last = abs(macd_z_score.iloc[-1])
            
            # 條件判斷
            if close_last > upper_last and macd_z_last < 3:
                print(f'{stock_code} 股票最後一天的收盤價高於布林通道上線，MACD Z-score在3個標準差內')
                paint(df, macd, signal, hist, upper_band, middle_band, lower_band, stock_code)
            elif close_last < lower_last and macd_z_last < 3:
                print(f'{stock_code} 股票最後一天的收盤價低於布林通道下線，而且MACD Z-score在3個標準差內')
            elif lower_last < close_last < upper_last and macd_z_last < 3:
                print(f'{stock_code} 股票最後一天的收盤價在布林通道中間，MACD Z-score在3個標準差內')
            elif close_last > upper_last and macd_z_last >= 3:
                print(f'{stock_code} 股票最後一天的收盤價高於布林通道上線，MACD Z-score不在3個標準差內')
            elif close_last < lower_last and macd_z_last >= 3:
                print(f'{stock_code} 股票最後一天的收盤價低於布林通道下線，而且MACD Z-score不在3個標準差內')
            elif lower_last < close_last < upper_last and macd_z_last >= 3:
                print(f'{stock_code} 股票最後一天的收盤價在布林通道中間，但MACD Z-score不在3個標準差內')
            else:
                print(f'{stock_code} 的情況未被特別處理。')
        else:
            print(f'{stock_code} 的DataFrame為空。')
    except Exception as e:
        print(f"處理 {stock_code} 時發生錯誤: {e}")