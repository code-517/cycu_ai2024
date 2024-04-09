#/workspaces/cycu_ai2024/20240409/mapdata202301070205/地震活動彙整_638482837875965379.csv
#/workspaces/cycu_ai2024/20240409/mapdata202301070205/COUNTY_MOI_1090820.shp
import pandas as pd
import folium

# 讀取CSV檔案
# 讀取CSV檔案，指定編碼為'big5'
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson

# 讀取CSV檔案，指定編碼為'big5'
earthquakes = pd.read_csv('/workspaces/cycu_ai2024/20240409/mapdata202301070205/地震活動彙整_638482870297236226.csv', encoding='big5')
earthquakes['地震時間'] = pd.to_datetime(earthquakes['地震時間'], errors='coerce')
earthquakes = earthquakes.dropna(subset=['地震時間'])
# 建立地圖，設定初始位置為台灣
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 建立一個用於存儲地震活動的GeoJson格式的列表
data = {
    "type": "FeatureCollection",
    "features": []
}
# 將'地震時間'欄位轉換為ISO 8601格式的日期時間字符串
earthquakes['地震時間'] = pd.to_datetime(earthquakes['地震時間']).dt.strftime('%Y-%m-%dT%H:%M:%S')
# 將地震活動加到GeoJson列表中
for index, row in earthquakes.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['經度'], row['緯度']]
        },
        "properties": {
            "time": row['地震時間'],
            "icon": "marker",
            "popup": f"地震時間：{row['地震時間']}<br>規模：{row['規模']}<br>經度：{row['經度']}<br>緯度：{row['緯度']}<br>位置：{row['位置']}",
        }
    }
    data["features"].append(feature)

# 將帶有時間軸的GeoJson添加到地圖上
TimestampedGeoJson(
    data,
    period="PT1H",
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=100,
    loop_button=True,
    date_options='YYYY/MM/DD HH:mm:ss',
    time_slider_drag_update=True
).add_to(m)

# 顯示地圖
m

# 存成html檔
m.save('map.html')