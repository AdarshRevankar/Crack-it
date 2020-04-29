import math

import matplotlib.pyplot as plt
import numpy as np

# Data
X = np.array([1, 3, 4, 5, 1, 4, 1, 2])
Y = np.array([3, 3, 3, 3, 2, 2, 1, 1])

# Data items
k = 2

# scatter plot
plt.scatter(X, Y)
plt.show()


def eucleadian_distance(x1, x2, y1, y2):
    # Distance between two data points
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Select initial centroid
m1 = (1, 1)
m2 = (2, 1)

prev_m1 = m1
prev_m2 = m2

while True:
    # distance from each centroid
    class_ = [0] * len(X)
    m1_pts_x = []
    m1_pts_y = []
    m2_pts_x = []
    m2_pts_y = []
    SSE = 0
    print('m1', ' ', 'm2', ' ', 'class')
    for i, x, y in zip(range(len(X)), X, Y):
        dist_m1 = eucleadian_distance(m1[0], x, m1[1], y)
        dist_m2 = eucleadian_distance(m2[0], x, m2[1], y)
        class_[i] = 1 if dist_m1 < dist_m2 else 2
        print(round(dist_m1, 2), ' ', round(dist_m2, 2), ' ', class_[i])
        if class_[i] == 1:
            SSE += dist_m1 ** 2
            m1_pts_x.append(x)
            m1_pts_y.append(y)
        else:
            SSE += dist_m2 ** 2
            m2_pts_x.append(x)
            m2_pts_y.append(y)

    plt.scatter(m1_pts_x, m1_pts_y, c='red')
    plt.scatter(m2_pts_x, m2_pts_y, c='black')
    plt.show()

    # Goodness of cluster
    # Between cluser variation
    BCV = eucleadian_distance(m1[0], m2[0], m1[1], m2[1])

    BCV_WCV = BCV / SSE
    print('BCV / WCV = Between cluser Var. / Within Cluster variation = ', BCV_WCV)

    # Identifying new centroid
    # M1
    prev_m1 = m1
    prev_m2 = m2
    m1 = (sum(m1_pts_x) / len(m1_pts_x), sum(m1_pts_y) / len(m1_pts_y))
    m2 = (sum(m2_pts_x) / len(m2_pts_x), sum(m2_pts_y) / len(m2_pts_y))
    print('New centroid: ', m1, m2)

    if prev_m1[0] == m1[0] and prev_m1[1] == m1[1] and prev_m2[0] == m2[0] and prev_m2[1] == m2[1]:
        break
