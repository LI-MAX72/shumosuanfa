from sympy  import *
from scipy.integrate import odeint
from numpy import arange
"""求解解析解"""
# y  = symbols('y',cls = Function)
# x = symbols('x')
# eq = Eq(y(x).diff(x,3)+2*y(x).diff(x,1)+y(x),x*x)
# print(dsolve(eq,y(x)))
"""求解数值解"""
dy = lambda y,x: x**2+y**2
x = arange(0,10.5,0.5)
sol = odeint(dy,0,x)
print("x={}\n对应的数值解析y={}".format(x,sol.T))
