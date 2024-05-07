#/workspaces/cycu_ai2024/20240507/11022345_1.csv
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 讀取CSV文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240507/11022345_1.csv')
#把第二欄刪掉
df = df.drop(df.columns[2], axis=1)
# 對時間欄位做標準化，把他切分為每個五分鐘(1-288)
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.hour*12 + df['time'].dt.minute/5
df['time'] = df['time'].astype(int)

# 將'gate'欄位分解為'road', 'mileage'和'direction'
df['mileage'] = df['gate'].str.slice(3, 7).astype(int)
df['direction'] = df['gate'].str.slice(-1)

# 將'road'和'direction'欄位轉換為數字
df['direction'] = df['direction'].map({'N': 0, 'S': 1})

# 刪除原始的'gate'欄位
df = df.drop(columns=['gate'])
print(df)
#以x軸為時間，y軸為mileage，Z為車輛數也就是第二欄，顏色為速度畫出四維圖
#速度的分色為藍色到紅色
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

# 刪除或填充NaN值
df = df.dropna()

# 限制無窮大的值
df = df[np.isfinite(df['31小客車速度'])]

# 創建一個3D圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定義顏色和範圍
colors = ['white', 'purple', 'red', 'orange', 'yellow', 'green']
bounds = [-1, 0, 20, 40, 60, 80, 160]
norm = BoundaryNorm(bounds, len(colors))
cmap = ListedColormap(colors)

# 繪製散點圖，其中x軸為時間，y軸為里程數，z軸為車輛數，顏色為速度
sc = ax.scatter(df['time'], df['mileage'], df['31小客車'], c=df['31小客車速度'], cmap=cmap, norm=norm)

# 添加顏色條
plt.colorbar(sc)

# 設置軸標籤
ax.set_xlabel('Time')
ax.set_ylabel('Mileage')
ax.set_zlabel('Number of Cars')

# 顯示圖形
plt.show()
#圖形存下來
plt.savefig('/workspaces/cycu_ai2024/20240507/11022345_2.png')