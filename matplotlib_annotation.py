import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1
plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color='b')  # 用散点来表示，如果设置有参数，就会显示x0，y0这个点，s代表大小
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)  # 显示两个点之间的一条直线，k--简写，k黑色--虚线，lw线宽

# method 1
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext =(+30,-30),
             textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
# 选择对x0，y0进行标注，xycoords='data'是说基于数据的值来选位置，
# xytext =(+30,-30)和textcoords='offset points对于标注的位置的描述和xy的偏差值
# arrowprops是对箭头的一些设置

plt.text(-3.7,3,r'$thie\ is\ the\ some\ text$',fontdict={'size':16,'color':'r'})
# 其中3.7,3是表示选取文本的位置，x坐标-3.7，y坐标3的文本
plt.show()