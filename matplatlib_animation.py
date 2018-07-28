import  numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
# subplots返回的值的类型为元组，其中包含两个元素：第一个为一个画布，第二个是子图
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

# 定义一个animation函数
def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,  # 大都好是因为返回的是一个列表，用逗号直接选第一个
def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=True)
# frames是帧数,init_func 最开始的动画是什么样的,interval 多少毫秒更新一次，blit是不是更新整张动画
plt.show()