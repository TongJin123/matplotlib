import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2) # 这个函数是计算山体高度的函数

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 生成-3到3，n个线段
X, Y = np.meshgrid(x, y) # 把xy绑定成网格的输入值

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#  contourf只是填充等高线
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
#  contour生成等高线，cmap是把数字对应的颜色在cmap找，就是每个数字对应不同的颜色,8就是等高线分成10部分，因为0是2部分
plt.clabel(C,inline=False,fontsize=10)
# 数字书否被等高线覆盖，True就是确定,
plt.xticks(())
plt.yticks(())
plt.show()