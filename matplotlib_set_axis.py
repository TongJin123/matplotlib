import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
plt.plot(x, y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))  # 设置x的取值范围
plt.ylim((-2,3))  # 设置y的取值范围
plt.xlabel("I am x")    # 设置对x轴的描述
plt.ylabel("I am y")    # 设置对y轴的描述
new_ticks = np.linspace(-1,2,5)  # 替换角标，-1到2，分5个单位，角标就变成-1到2的五间隔一样的值
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r"$really\ bad$",r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
# 把y轴角标换成状态（也就是后面一一对应的英文单词）
# 把单词改成机器能读的，数学类型的字体，前后加$，因为空格识别不出来，必须加上\转义一下
# 加上r就是正则匹配，匹配$里面的内容 alpha数学里面的a阿尔法

# gca  'get current axis'
ax = plt.gca()  # 这个轴就是plt出来的一张图
ax.spines['right'].set_color('none')  # spines脊梁，就是把右边框设置为none
ax.spines['top'].set_color('none')  # 把上边框设置为none
ax.xaxis.set_ticks_position('bottom')  # x轴用下边框的坐标轴代替
ax.yaxis.set_ticks_position('left')     # y轴用左边框代替
ax.spines['bottom'].set_position(('data',-1))  # 横坐标的原点是纵坐标的-1
ax.spines['left'].set_position(('data',0))  # 把纵坐标的原点放在横坐标的0
# outward ， axes 定位到百分比的位置
plt.show()