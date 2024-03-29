##使用curve_fit

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#自定义函数 e指数形式
def func(x, a, b):
 return a+b*x*x

#定义x、y散点坐标
x = [19,25,31,38,44]
x = np.array(x)
num = [19,32.3,49,73.3,97.8]
y = np.array(num)

#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
yvals = func(x,a,b) #拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
