#C:\Users\User\Desktop\1\cycu_ai2024\20240430\combinedM05A.csv
#C:\Users\User\Desktop\1\cycu_ai2024\20240521\國道計費門架座標及里程牌價表1130327.csv
import pandas as pd
import folium

# 讀取CSV檔案
df = pd.read_csv(r'C:\Users\User\Desktop\1\cycu_ai2024\20240430\combinedM05A.csv')

# 讀取閘門位置的CSV檔案
gate_df = pd.read_csv(r'C:\Users\User\Desktop\1\cycu_ai2024\20240521\國道計費門架座標及里程牌價表1130327.csv')

# 創建閘門位置的字典
gate_locations = gate_df.set_index('設定收費區代碼')[['緯度', '經度']].T.to_dict('list')

# 創建Folium地圖對象
m = folium.Map(location=[25.0339639, 121.5644722], zoom_start=13)  # 這裡的緯度和經度是假設的，你需要替換它們

# 在地圖上標記每個時間點的車速
for index, row in df.iterrows():
    # 獲取閘門的緯度和經度
    lat, lon = gate_locations[row['gate']]
    
    # 創建一個標記
    marker = folium.Marker(
        location=[lat, lon],
        popup=f"Car Type: {row['Value1']}, Speed: {row['Value2']}, Traffic Volume: {row['Value3']}",
    )
    # 將標記添加到地圖上
    marker.add_to(m)

# 儲存地圖
m.save('map.html')