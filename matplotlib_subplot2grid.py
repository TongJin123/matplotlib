import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# (3,3)是整个figure，3行3列，从原点开始plot，colspan代表有多少单位的列，rowspan有多少行，默认1
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')  # 设置figuer的title
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[2,0])
ax5 = plt.subplot(gs[2,1])
# 使用索引的方式告诉我们占了那些行那些列

f,((ax11,ax12),(ax21,ax22)) =plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[2,1])
# 四个图共享x，y轴  sharex=True,sharey=True
plt.tight_layout()
plt.show()
