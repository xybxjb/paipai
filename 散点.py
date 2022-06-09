import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['STKAITI']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#cc00ff'
fig = plt.figure(figsize=(10, 8), facecolor='#cc00ff')
ax = Axes3D(fig)
delta = 0.125
# 生成代表X轴数据的列表
x = np.arange(-4.0, 4.0, delta)
# 生成代表Y轴数据的列表
y = np.arange(-3.0, 4.0, delta)
# 对x、y数据执行网格化
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
# 计算Z轴数据（高度数据）
Z = (Z1 - Z2) * 2
# 绘制3D图形
ax.scatter(X, Y, Z,
           c='green',
           edgecolors='red')
plt.xlabel('X轴', fontsize=15)
plt.ylabel('Y轴', fontsize=15)
ax.set_zlabel('Z轴', fontsize=15)
ax.set_title('《散点图》', y=1.02, fontsize=25, color='gold')
# 设置Z轴范围
ax.set_zlim(-2, 2)
plt.show()

