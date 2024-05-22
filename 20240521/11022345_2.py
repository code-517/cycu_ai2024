#C:\Users\User\Desktop\1\cycu_ai2024\20240430\combinedM05A.csv
#C:\Users\User\Desktop\1\cycu_ai2024\20240521\國道計費門架座標及里程牌價表1130327.csv
#//////
#/workspaces/cycu_ai2024/20240521/國道計費門架座標及里程牌價表1130327.csv
#/workspaces/cycu_ai2024/20240521/M05A31_rows.csv
#/workspaces/cycu_ai2024/20240521
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
import json

# 讀取CSV檔案
df = pd.read_csv(r'/workspaces/cycu_ai2024/20240521/M05A31_rows.csv')

# 讀取閘門位置的CSV檔案
gate_df = pd.read_csv(r'/workspaces/cycu_ai2024/20240521/國道計費門架座標及里程牌價表1130327.csv')

# 創建閘門位置的字典
gate_locations = gate_df.set_index('設定收費區代碼')[['緯度', '經度']].T.to_dict('list')

# 創建Folium地圖對象
m = folium.Map(location=[25.0339639, 121.5644722], zoom_start=13)

# 創建GeoJSON對象
geo_json_data = {
    'type': 'FeatureCollection',
    'features': []
}

# 在GeoJSON對象中添加每個時間點的車速
# 在GeoJSON對象中添加每個時間點的車速
for index, row in df.iterrows():
    # 獲取閘門的緯度和經度
    lat, lon = gate_locations[row['GantryFrom']]
    
    # 將時間欄位轉換為datetime對象
    time = pd.to_datetime(row['Time'])
    
    # 創建一個特徵
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat]
        },
        'properties': {
            'time': time.isoformat(),
            'popup': f"Car Type: {row['車種小客車']}, Speed: {row['SpaceMeanSpeed']}, Traffic Volume: {row['Traffic']}",
            'icon': 'circle',
            'iconstyle': {
                # ...
            }
        }
    }
    # 將特徵添加到GeoJSON對象中
    geo_json_data['features'].append(feature)
    # 將特徵添加到GeoJSON對象中
    geo_json_data['features'].append(feature)

# 在地圖上添加帶有時間軸的GeoJSON
TimestampedGeoJson(
    geo_json_data,
    period='PT1H',  # 這裡的'PT1H'表示每個時間點之間的間隔為1小時，你需要根據你的資料來調整這個值
    add_last_point=True,
).add_to(m)

# 儲存地圖
m.save('map.html')