import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
def fun(t,w):
    x = w[0]
    y = w[1]
    z = w[2]
    return [2*x-3*y+3*z,4*x-5*y+3*z,4*x-4*y+2*z]

y0 = [1,2,1]
yy = solve_ivp(fun,(0,10),y0,method='RK45',t_eval = np.arange(1,10,1))

t = yy.t
data = yy.y
plt.plot(t,data[0,:],label = "x")
plt.plot(t,data[1,:],label = "y")
plt.plot(t,data[2,:],label = "z")
plt.xlabel("时间s")
plt.show()
