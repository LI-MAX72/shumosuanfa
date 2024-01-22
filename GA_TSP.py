import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

num_points = 38

#points_coordinate = np.random.rand(num_points, 2)  # generate coordinate of points
points_coordinate = [
    [11003.611100, 42102.500000],
    [11108.611100, 42373.888900],
    [11133.333300, 42885.833300],
    [11158.055600, 42106.388900],
    [11158.055600, 42106.388900],
    [11158.055600, 42106.388900],
    [11283.333300, 42983.333300],
    [11360.833300, 43242.777800],
    [11416.666700, 42983.333300],
    [11423.888900, 43000.277800],
    [11438.333300, 42057.222200],
    [11461.111100, 43252.777800],
    [11485.555600, 43187.222200],
    [11503.055600, 42855.277800],
    [11511.388900, 42106.388900],
    [11522.222200, 42841.944400],
    [11569.444400, 43136.666700],
    [11583.333300, 43150.000000],
    [11595.000000, 43148.055600],
    [11600.000000, 43150.000000],
    [11690.555600, 42686.666700],
    [11715.833300, 41836.111100],
    [11751.111100, 42814.444400],
    [11770.277800, 42651.944400],
    [11785.277800, 42884.444400],
    [11822.777800, 42673.611100],
    [11846.944400, 42660.555600],
    [11963.055600, 43290.555600],
    [11973.055600, 43026.111100],
    [12058.333300, 42195.555600],
    [12149.444400, 42477.500000],
    [12286.944400, 43355.555600],
    [12300.000000, 42433.333300],
    [12355.833300, 43156.388900],
    [12363.333300, 43189.166700],
    [12372.777800, 42711.388900],
    [12386.666700, 43334.722200],
    [12421.666700, 42895.555600],
    [12645.000000, 42973.333300]
]
points_coordinate = np.array(points_coordinate)
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')


def cal_total_distance(routine):
    '''The objective function. input routine, return total distance.
    cal_total_distance(np.arange(num_points))
    '''
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])
from sko.GA import GA_TSP

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_points, size_pop=50, max_iter=1000, prob_mut=1)
best_points, best_distance = ga_tsp.run()
fig, ax = plt.subplots(1, 2)
best_points_ = np.concatenate([best_points, [best_points[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax[0].plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
ax[1].plot(ga_tsp.generation_best_Y)
print(ga_tsp.best_y)
plt.show()
