import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['STKAITI']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#cc00ff'
fig = plt.figure(figsize=(12, 10), facecolor='#cc00ff')
ax = Axes3D(fig)
delta = 0.125
# 生成代表X轴数据的列表
x = np.linspace(-2, 2, 10)
# 生成代表Y轴数据的列表
y = np.linspace(-2, 2, 10)
# 对x、y数据执行网格化
X, Y = np.meshgrid(x, y)

# 计算Z轴数据（高度数据）
Z = X**2 - Y**2
# 绘制3D图形
ax.plot_surface(X, Y, Z,
    rstride=1,  # rstride（row）指定行的跨度
    cstride=1,  # cstride(column)指定列的跨度
    cmap=plt.get_cmap('rainbow'))  # 设置颜色映射
plt.xlabel('X轴', fontsize=15)
plt.ylabel('Y轴', fontsize=15)
ax.set_zlabel('Z轴', fontsize=15)
ax.set_title('《曲面图》', y=1.02, fontsize=25, color='gold')
plt.show()

