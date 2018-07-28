import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  # 定义一个figure
ax = Axes3D(fig)  # 在figure里面添加一个3Daxes

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)  # 把X，Y  meshgrid到底面的面上去
R = np.sqrt(X**2+Y**2)  # 计算方程生成一个新的值，新值作为高度
Z = np.sin(R)  # 生成高度

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# 生成3D图像，rstride行跨度，跨度越小越密集，cstride列跨度

ax.contourf(X,Y,Z,zdir='',offset=-2,cmap=plt.get_cmap('rainbow'))
# zdir等高线从那个轴压下去 ，offset是把等高线压到z=-2的位置
ax.set_zlim(-2,2)  # z的范围 -2到 2
plt.show()
