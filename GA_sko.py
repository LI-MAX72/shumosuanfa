import numpy as np
from sko.GA import GA
import pandas as pd
import matplotlib.pyplot as plt
def schaffer(p):
    '''
    This function has plenty of local minimum, with strong shocks
    global minimum at (0,0) with value 0
    '''
    x = np.array(p)
    return (x[0]-2)*(x[0]-2)+(x[1]-1)*(x[1]-1)
    # x1, x2 = p
    # x = np.square(x1) + np.square(x2)
    # return 0.5 + (np.square(np.sin(x)) - 0.5) / np.square(1 + 0.001 * x)
def s1(x):
    return x[1]*2-x[0]-1
def s2(x):
    return x[1]*x[1]-0.25*x[0]*x[0]-1
s = [s1,s2]
ga = GA(func=schaffer, n_dim=2, size_pop=100, max_iter=800, prob_mut=0.001, lb=[-1, -1], ub=[1, 1],constraint_ueq = s , precision=1e-7)
best_x, best_y = ga.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)


Y_history = pd.DataFrame(ga.all_history_Y)
fig, ax = plt.subplots(2, 1)
ax[0].plot(Y_history.index, Y_history.values, '.', color='red')
Y_history.min(axis=1).cummin().plot(kind='line')
plt.show()
