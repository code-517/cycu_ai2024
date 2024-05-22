#/workspaces/cycu_ai2024/20240521/國道計費門架座標.csv
#/workspaces/cycu_ai2024/20240521/M05A31_2rows.csv
import pandas as pd
from folium.plugins import TimestampedGeoJson
import folium

# 讀取門架座標資料
df_gantry = pd.read_csv('/workspaces/cycu_ai2024/20240521/國道計費門架座標.csv')

# 讀取車流量資料
df_traffic = pd.read_csv('/workspaces/cycu_ai2024/20240521/M05A31_2rows.csv')

# 創建門架座標的字典
gantry_locations = {row['設定收費區代碼']: (row['緯度'], row['經度']) for index, row in df_gantry.iterrows()}

# 創建地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 在地圖上添加閘門的位置
for gantry, location in gantry_locations.items():
    folium.CircleMarker(location, radius=5, color='blue', fill=True, fill_color='blue', fill_opacity=0.6).add_to(m)

# 在地圖上添加每個時間點的車流量和速度
for index, row in df_traffic.iterrows():
    # 獲取閘門的緯度和經度
    lat, lon = gantry_locations[row['GantryFrom']]
    
    # 根據速度設定線條的顏色
    if row['SpaceMeanSpeed'] < 60:
        color = 'red'
    elif row['SpaceMeanSpeed'] < 70:
        color = 'orange'
    elif row['SpaceMeanSpeed'] < 80:
        color = 'yellow'
    else:
        color = 'green'
    
    # 在地圖上添加線條
    folium.PolyLine([(lat, lon), (lat, lon)], color=color).add_to(m)

# 儲存地圖
m.save('map.html')