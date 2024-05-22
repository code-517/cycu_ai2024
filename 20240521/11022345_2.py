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

# 在GeoJSON對象中添加每個時間點的車流量和速度
for index, row in df.iterrows():
    # 獲取閘門的緯度和經度
    lat, lon = gate_locations[row['GantryFrom']]
    
    # 將時間欄位轉換為datetime對象
    time = pd.to_datetime(row['Time'])
    
    # 根據速度設定線的顏色
    if row['SpaceMeanSpeed'] < 90:
        color = 'red'
    else:
        color = 'green'
    
    # 創建一個特徵
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'LineString',
            'coordinates': [[lon, lat], [lon, lat]],  # 這裡需要你的資料中有閘門的起點和終點的緯度和經度
        },
        'properties': {
            'times': [time.isoformat(), time.isoformat()],
            'style': {
                'color': color,
                'weight': row['Traffic'] / 100,  # 這裡假設車流量的最大值為100，你需要根據你的資料來調整這個值
            },
            'popup': f"Car Type: {row['車種小客車']}, Speed: {row['SpaceMeanSpeed']}, Traffic Volume: {row['Traffic']}",
        }
    }
    
    # 將特徵添加到GeoJSON對象中
    geo_json_data['features'].append(feature)

# 在地圖上添加TimestampedGeoJson
TimestampedGeoJson(
    geo_json_data,
    period='PT5M',  # 每五分鐘更新一次
    add_last_point=True,
).add_to(m)

# 儲存地圖
m.save('map.html')