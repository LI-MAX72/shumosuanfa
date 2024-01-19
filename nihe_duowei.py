import numpy as np
from scipy.optimize import curve_fit
# 创建一个函数模型用来生成数据
def func1(x, a,b):
    r = np.exp(-a*x[0])*np.sin(b*x[1])+x[2]*x[2]
    return r.ravel()

# 生成原始数据
# xx = np.indices([10, 10])
# z = func1(xx, 10, 5, 2, 5) + np.random.normal(size=100)/100
xx = np.array([[23.73,22.34,28.84,27.47,20.73],[5.49,4.32,5.04,4.72,5.35],[1.21,1.35,1.92,1.49,1.56]])
z = np.array([15.02,12.62,14.86,13.98,15.91])
ab, para = curve_fit(func1, xx, z)
print(ab)
# [10.00258587  5.00146314  1.99952885  5.00138184]
