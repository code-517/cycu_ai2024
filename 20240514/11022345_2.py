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
print(selected_rows)
x = x.dropna()

# 取出第五個欄位的值
y = selected_rows.iloc[:, 4]

# 轉換為陣列
x = np.array(x)

# 生成隨機數據
np.random.seed(0)
x_rand = np.random.normal(0, 1, 100)
y_rand = np.random.normal(0, 1, 100)
z_rand = x_rand**3 + y_rand**3 + 3*x_rand**2*y_rand + 3*x_rand*y_rand**2 + np.random.normal(0, 0.1, 100)

# 建立立方擬合模型
coefficients = np.polyfit(x_rand + y_rand, z_rand, 3)
model = np.poly1d(coefficients)

# 使用擬合模型預測z值
z_pred = model(x_rand + y_rand)

# 繪製原始數據
plt.scatter(x_rand + y_rand, z_rand, label='original data')

# 繪製擬合模型
plt.plot(x_rand + y_rand, z_pred, color='red', label='cubic fit')

plt.legend()
plt.show()
#存下來