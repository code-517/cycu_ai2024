#/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500.csv
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
# 讀取CSV文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500.csv')

# 選擇第四個欄位值為31的行
selected_rows = df[df.iloc[:, 3] == 31]
#選擇第二個欄位值開頭為01F
selected_rows = selected_rows[selected_rows.iloc[:, 1].apply(lambda x: x.startswith('01F'))]
# 選擇第三個欄位值為N的行
selected_rows = selected_rows[selected_rows.iloc[:, 2] == 'N']
# 提取第二個欄位中的數字，只有當數字長度為4時
x = selected_rows.iloc[:, 1].apply(lambda x: int(re.search(r'\d{4}', x).group()) if re.search(r'\d{4}', x) else None)

# 去除x中的None值
selected_rows = selected_rows[x.notnull()]
x = x.dropna()

# 取出第五個欄位的值
y = selected_rows.iloc[:, 4]

# 轉換為陣列
x = np.array(x)
y = np.array(y)

# 設定 numpy 的列印選項以抑制科學記數法
np.set_printoptions(suppress=True)
from scipy.interpolate import CubicSpline

# 建立一個三次樣條曲線
cs = CubicSpline(x, y)

# 計算曲線上的值
x_new = np.arange(min(x), max(x), 0.1)
y_new = cs(x_new)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='original data')
plt.plot(x_new, y_new, label='cubic spline')
plt.legend(loc='best')
plt.show()
#標題11022345WUYICH 國道一號北向
plt.title('11022345WUYICH 1_North')
#x軸標題KM
plt.xlabel('KM')
#y軸標題V
plt.ylabel('V')
#存下來
plt.savefig('/workspaces/cycu_ai2024/20240514/11022345_2D_N.png')
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 選擇第四個欄位值為31的行
selected_rows = df[df.iloc[:, 3] == 31]
#選擇第二個欄位值開頭為01F
selected_rows = selected_rows[selected_rows.iloc[:, 1].apply(lambda x: x.startswith('01F'))]
# 選擇第三個欄位值為N的行
selected_rows = selected_rows[selected_rows.iloc[:, 2] == 'S']
# 提取第二個欄位中的數字，只有當數字長度為4時
x = selected_rows.iloc[:, 1].apply(lambda x: int(re.search(r'\d{4}', x).group()) if re.search(r'\d{4}', x) else None)

# 去除x中的None值
selected_rows = selected_rows[x.notnull()]
x = x.dropna()

# 取出第五個欄位的值
y = selected_rows.iloc[:, 4]

# 轉換為陣列
x = np.array(x)
y = np.array(y)
print(x)
# 設定 numpy 的列印選項以抑制科學記數法
np.set_printoptions(suppress=True)
from scipy.interpolate import CubicSpline

# 建立一個三次樣條曲線
cs = CubicSpline(x, y)

# 計算曲線上的值
x_new = np.arange(min(x), max(x), 0.1)
y_new = cs(x_new)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='original data')
plt.plot(x_new, y_new, label='cubic spline')
plt.legend(loc='best')
plt.show()
#標題11022345WUYICH 國道一號北向
plt.title('11022345WUYICH 1_south')
#x軸標題KM
plt.xlabel('KM')
#y軸標題V
plt.ylabel('V')
#存下來
plt.savefig('/workspaces/cycu_ai2024/20240514/11022345_2D_N.png')
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

