import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt

num_points = 31

points_coordinate  =  [
    [1304, 2312],
    [3639, 1315],
    [4177, 2244],
    [3712, 1399],
    [3488, 1535],
    [3326, 1556],
    [3238, 1229],
    [4196, 1004],
    [4312, 790],
    [4386, 570],
    [3007, 1970],
    [2562, 1756],
    [2788, 1491],
    [2381, 1676],
    [1332, 695],
    [3715, 1678],
    [3918, 2179],
    [4061, 2370],
    [3780, 2212],
    [3676, 2578],
    [4029, 2838],
    [4263, 2931],
    [3429, 1908],
    [3507, 2367],
    [3394, 2643],
    [3439, 3201],
    [2935, 3240],
    [3140, 3550],
    [2545, 2357],
    [2778, 2826],
    [2370, 2975]
]
points_coordinate = np.array(points_coordinate)
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')

alpha = 1;
beta = 5;
rho = 0.1;

def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


# %% Do ACA
from sko.ACA import ACA_TSP

aca = ACA_TSP(func=cal_total_distance, n_dim=num_points,
              size_pop=50, max_iter=200,
              distance_matrix=distance_matrix,alpha = alpha,beta = beta,rho = rho)

best_x, best_y = aca.run()

print(best_x)
print(best_y)
# %% Plot
fig, ax = plt.subplots(1, 2)
best_points_ = np.concatenate([best_x, [best_x[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax[0].plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
pd.DataFrame(aca.y_best_history).cummin().plot(ax=ax[1])
plt.show()
