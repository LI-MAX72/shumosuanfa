# -*- coding: utf-8 -*-
#比较抽象，拟合效果比较一般
"""
演示二维插值。
"""
# -*- coding: utf-8 -*-
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from scipy import interpolate
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def func(x, y):
    return (x+y)*np.exp(-5.0*(x**2 + y**2))

# X-Y轴分为20*20的网格
# x = np.linspace(-1, 1, 20)
# y = np.linspace(-1,1,20)
x = np.array([129,140,103.5,88,185.5,195,105,157.5,107.5,77,81,162,162,117.5])
y = np.array([7.5,141.5,23,147,22.5,137.5,85.5,-6.5,-81,3,56.5,-66.5,84,-33.5])
x, y = np.meshgrid(x, y)#20*20的网格数据

#fvals = func(x,y) # 计算每个网格点上的函数值  15*15的值
z = np.array([4,8,6,8,6,8,8,9,9,8,8,9,4,9])

z_grid = np.zeros((len(x),len(y)))

for i in range(len(x)):
    z_grid[i][i] = z[i]
print(z_grid)
fig = plt.figure(figsize=(9, 6))
#Draw sub-graph1
ax=plt.subplot(1, 2, 1,projection = '3d')
surf = ax.plot_surface(x, y, z_grid, rstride=2, cstride=2, cmap=cm.coolwarm,linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.colorbar(surf, shrink=0.5, aspect=5)#标注

#二维插值
newfunc = interpolate.interp2d(x, y, z_grid, kind='cubic')#newfunc为一个函数

# 计算100*100的网格上的插值
xnew = np.linspace(77,195,200)#x
ynew = np.linspace(-81,141.5,200)#y
fnew = newfunc(xnew, ynew)#仅仅是y值   100*100的值  np.shape(fnew) is 100*100
xnew, ynew = np.meshgrid(xnew, ynew)
ax2=plt.subplot(1, 2, 2,projection = '3d')
surf2 = ax2.plot_surface(xnew, ynew, fnew, rstride=2, cstride=2, cmap=cm.coolwarm,linewidth=0.5, antialiased=True)
ax2.set_xlabel('xnew')
ax2.set_ylabel('ynew')
ax2.set_zlabel('fnew(x, y)')
plt.colorbar(surf2, shrink=0.5, aspect=5)#标注

plt.show()
