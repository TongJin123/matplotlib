import matplotlib.pyplot as plt
import matplotlib.gridspec

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])  # 必须加上中括号
ax1.plot(x,y,'r')   # ‘r’表示的是颜色
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])  # 必须加上中括号
ax2.plot(x,y,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('btitle')

plt.axes([.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'g')  # 把y的值逆序一下
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')
# 不必定义一个对象，因为在设置的时候会设置的上面最近的plot

plt.show()