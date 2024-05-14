import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240507/11022345_1.csv')

# 對時間欄位做標準化，把他切分為每個五分鐘(1-288)
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.hour*12 + df['time'].dt.minute/5
df['time'] = df['time'].astype(int)
# 選擇第二個欄位值開頭為 '01F' 和第三個欄位值為 'S' 的行
df = df[(df.iloc[:, 1].str.startswith('01F')) & (df.iloc[:, 2] == 'S')]

# 從第二個欄位中取得四位數字
df['four_digits'] = df.iloc[:, 1].str[3:7]

# 將 'four_digits' 轉換為數值
df['four_digits'] = pd.to_numeric(df['four_digits'])

# 提取里程數據
y = df['four_digits'].values
# 選擇第二個欄位值開頭為 '01F' 和第三個欄位值為 'S' 的行
df = df[(df.iloc[:, 1].str.startswith('01F')) & (df.iloc[:, 2] == 'S')]
# 提取時間數據
x = df['time'].values

# 選擇第四個欄位的數據
z = df.iloc[:, 3].values

# 將數據轉換為適合 griddata 的格式
points = np.array([x, y]).T
values = z

# 創建一個規則的網格
grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]

# 使用 griddata 進行插值
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

# 創建一個 3D 圖形
fig = plt.figure(figsize=(20, 15))

# 繪製四個視角的圖形
# 繪製四個視角的圖形
for i in range(4):
    ax = fig.add_subplot(2, 2, i+1, projection='3d')
    surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')  # 使用 'viridis' 顏色映射
    ax.view_init(elev=20., azim=i*90)
    ax.set_xlabel('Time')
    ax.set_ylabel('Mileage')
    ax.set_zlabel('Traffic Volume')

# 添加顏色條
fig.colorbar(surf, shrink=0.5, aspect=5)

#標題11022345WUYICH_S
plt.suptitle('11022345WUYICH_S', fontsize=16)

plt.show()

# 儲存圖片
plt.savefig('/workspaces/cycu_ai2024/20240514/11022345_3D.png')