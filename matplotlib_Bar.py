import matplotlib.pyplot as plt
import numpy as np

n = 12   # 有十二个柱状图
X = np.arange(n)  # X生成0-11数字
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)  # random.uniform从0.5到1这个范围的数值，生成n个
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
# 设置柱状图，柱状图的xy坐标，facecolor主体的颜色，edgecolor边框颜色

for x,y in zip(X,Y1):  # zip函数可以把X，Y1的值返回两个变量
    # ha：horizontal alignment
    plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')
    # 在柱状图上面添加数值y1的值，横向对齐是居中，纵向对齐的方式是bottom
for x,y in zip(X,Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    # 因为柱状图的是-Y2，所以便利出来的y应变成负数，才能和柱状图对应
plt.xlim(-0.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()