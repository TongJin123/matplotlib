import  matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 =  -1*y1


fig ,ax1 = plt.subplots()  # 创建一个subplots，因为用到两个轴，
ax2 = ax1.twinx()  #把ax1颠倒过来，使用镜面
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='b')

plt.show()