import numpy as np
import matplotlib.pyplot as plt

#定义x、y散点坐标——你自己的数据
x = [19,25,31,38,44]
x = np.array(x)
print('x is :\n',x)
num = [19,32.3,49,73.3,97.8]
y = np.array(num)

my_rho = np.corrcoef(x, y)

print("rho is:")
print(my_rho)
print('y is :\n',y)

#用n次多项式拟合，此处n = 3，设置为3-7都比较合理，视案例复杂度以及需求而定
f1 = np.polyfit(x, y, 2)
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
