import matplotlib.pyplot as plt
import numpy as np
a = np.random.random((3,3))  # 生成3行3列的0-1数字的矩阵
print(a)
plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')
# 展示图片，interpolation是image自带的风格
# cmap=plt.cm.bone 还可以传个字符串，lower是把形状反过来看(矩阵元素的大小不同位置也不同)，upper图片显示和矩阵是一致的，就是正常的
plt.colorbar(shrink=0.9)
# colorbar是图片旁边的标注，shrink压缩成90%,
plt.xticks(())
plt.yticks(())
plt.show()