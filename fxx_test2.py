import numpy as np
from scipy.optimize import minimize
import math
###不等式采用大于形式
if __name__ == '__main__':
    def objective(x):
        return math.exp(x[0])*(4*x[0]*x[0]+2*x[1]*x[1]+4*x[0]*x[1]+2*x[1]+1)
    def constraint1(x):
        return -1.5+x[0]+x[1]-x[0]*x[1]
    def constraint2(x):
        return  x[0]*x[1]+10
    x0 = np.array([0,0])
    solution = minimize(objective, x0, method='SLSQP', constraints=[{'fun': constraint1, 'type': 'ineq'},
                                                                   {'fun': constraint2, 'type': 'ineq'}])
    print(solution)
