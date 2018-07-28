import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)  # random.normal标准正态分布，在x轴随机生成1024个0-1数字
Y = np.random.normal(0,1,n)  # 在y轴随机生成1024个0-1的数字
T = np.arctan2(Y,X)  # 生成散点颜色

# plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# 生成散点图，s大小，c是颜色，alpha透明度
plt.scatter(np.arange(5),np.arange(5))
# 只看一条线的散点


# plt.xlim((-1.5,1.5))  #设置x轴的范围
# plt.ylim((-1.5,1.5))
plt.xticks(())  # 把x坐标隐藏
plt.yticks(())  # 把y坐标隐藏
plt.show()