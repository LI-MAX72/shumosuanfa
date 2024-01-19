import numpy as np
import matplotlib.pyplot as plt
x = np.array([-2, -1, 0, 1, 2])
y = 0.7*x+5
my_rho = np.corrcoef(x, y)#相关系数的核心代码
print(my_rho)
#用n次多项式拟合，此处n = 3，设置为3-7都比较合理，视案例复杂度以及需求而定
f1 = np.polyfit(x, y, 1)
print('f1 is :\n',f1)

#拟合y值
yvals = np.polyval(f1, x)
print('yvals is :\n',yvals)

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()
