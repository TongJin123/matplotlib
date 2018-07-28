import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel("I am x")
plt.ylabel("I am y")
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r"$really\ bad$",r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

l1, = plt.plot(x, y2,label='up')  # 给这条线设置一个名字，用label
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')  # 使用legend在figure中显示出线的名字
# 每条线都有一个返回值，返回值对象后面必须加上逗号，不然handle不能识别
# labels 是把handle里面的对象重新命名，loc是图例的位置，best是表示信息最少（最好）的地方显示，
# 如果重新命名一个名字，那么图例里面也只有这个名字
plt.show()