import numpy as np
from sko.PSO import PSO
#求最小
def fun_c(x):
    return -(-(x[0]-10)**2+x[0]*np.sin(x[0])*np.cos(2*x[0])-5*x*np.sin(3*x[0]))
max_iter = 150
pso = PSO(func = fun_c,n_dim = 1,pop = 60,max_iter = max_iter,lb = [0],ub = [20])
pso.record_mode = True
pso.run()
print('best_x is ', pso.gbest_x, 'best_y is', -pso.gbest_y)
