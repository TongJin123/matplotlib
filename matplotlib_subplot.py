import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1)  # 给定位置的描述，分成2行2列，第一张图
plt.plot([0,1],[0,1])  # 设置图的坐标范围,图形化
#
plt.subplot(2,3,4) # 给定位置的描述，分成2行2列，第二张图
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

plt.subplot(236)  # 也可以不用写逗号
plt.plot([0,1],[0,4])

# 把figure 如果想把第一张图占整个一列，那么第二张图必须从第二来本来的序号来排列，并设置好每行的个数

plt.show()