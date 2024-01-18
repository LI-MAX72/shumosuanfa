import numpy as np
from scipy.optimize import minimize
if __name__ == '__main__':
# 定义目标函数和约束条件
    def objective(x):
        return 5 * x[0] - 2 * x[1] + x[2]

    def constraint1(x):
        return x[0] + x[1] + x[2] - 1

    def constraint2(x):
        return 1 - x[0] ** 2 - x[1] ** 2 - x[2] ** 2

    def constraint3(x):
        return x[0] - x[2] ** 2

    def constraint4(x):
        return -x[0] - x[1] - x[2] + 1

    # 定义初始点
    x0 = np.array([0, 0, 0])

    # 使用SLSQP算法求解非线性规划问题
    solution = minimize(objective, x0, method='SLSQP', constraints=[{'fun': constraint1, 'type': 'eq'},
                                                                   {'fun': constraint2, 'type': 'ineq'},
                                                                   {'fun': constraint3, 'type': 'ineq'},
                                                                   {'fun': constraint4, 'type': 'ineq'}])

    print(solution)
