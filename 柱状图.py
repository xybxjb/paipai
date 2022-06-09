import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#cc00ff'
plt.rcParams['font.sans-serif'] = ['STKAITI']
# 创建画布
fig = plt.figure()
# 创建3D坐标系
axes3d = Axes3D(fig)
zs = range(5)
left = np.arange(0, 10)
height = np.array([])
for i in range(len(zs)):
    z = zs[i]
    np.random.seed(i)
    height = np.random.randint(0, 30, size=10)
    axes3d.bar(left, height, zs=z, zdir='x',
               color=['red', 'green', 'purple', 'yellow', 'blue', 'black', 'gray', 'orange', 'pink', 'cyan'])
plt.xticks(zs, ['1月份', '2月份', '3月份', '4月份', '5月份'])
plt.yticks(left, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G'])
plt.xlabel('月份')
plt.ylabel('型号')
plt.show()

