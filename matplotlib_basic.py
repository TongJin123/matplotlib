import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,5)  # x是从-1到1的50个点，相当于分成50段，分的越多越精确，有点像微分
# y = 2*x + 1
y = x**2     # 创建一个函数
plt.plot(x,y)  # 图形化函数
plt.show()   # 使用这个函数，图才会出来