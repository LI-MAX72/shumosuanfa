import numpy as np
from scipy.optimize import minimize
###不等式采用大于形式
if __name__ == '__main__':
    def objective(x):
        return 2*x[0]*x[0]-4*x[0]*x[1]+4*x[1]*x[1]-6*x[0]-3*x[1]
    def constraint1(x):
        return 3-x[0]-x[1]
    def constraint2(x):
        return  9-4*x[0]-x[1]
    def constraint3(x):
        return x[0]
    def constraint4(x):
        return x[1]
    x0 = np.array([0,0])
    solution = minimize(objective, x0, method='SLSQP', constraints=[{'fun': constraint1, 'type': 'ineq'},
                                                                   {'fun': constraint2, 'type': 'ineq'},
                                                                   {'fun': constraint3, 'type': 'ineq'},
                                                                   {'fun': constraint4, 'type': 'ineq'}])

    print(solution)
