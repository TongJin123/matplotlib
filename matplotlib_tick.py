import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1*x
plt.figure()
plt.plot(x,y,linewidth=10)
plt.ylim(-2,2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))

#  把xy的lable拿出来设置参数，设置字体大小set_fontsize，set_bbox设置方框，facecolor就是前面的颜色是什么，edgecolor边框颜色，alpha透明度
plt.show()