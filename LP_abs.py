
from scipy.optimize import linprog
import numpy as np
if __name__ == '__main__':
    c = np.array([1, 2, 3, 4, 1, 2, 3, 4])
    A_ub = np.array([[1, -1, -1, 1],
                     [1, -1, 1, -3],
                     [1, -1, -2, 3]])
    A_ub = np.hstack([A_ub, -A_ub])
    b_ub = np.array([[-2, -1, -1/2]])
    r = linprog(c, A_ub, b_ub, bounds=((0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None)))
    print(r)

    x = r.x[:4] - r.x[4:]

    print(f'求得最优解\nx_1 = {x[0]},\nx_2 = {x[1]},\nx_3 = {x[2]},\nx_4 = {x[3]},\n最优值 z = {r.fun}')
