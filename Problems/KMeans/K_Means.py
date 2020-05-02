import copy
import json
import math
from itertools import combinations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from Problems.KMeans.Utils import Z_Score_Normalization, print_table, nCr, show_plot, get_random_unique_indices


# ===========================================================
# HELPING FUNCTIONS
# ===========================================================

def euclidean_distance(point1, point2):
    # Distance between 2 data points
    return (((point1 - point2) ** 2).sum()) ** 0.5


# ===========================================================
# EXECUTION
# ===========================================================
# Data
config = json.load(open('config.json'))
data = pd.read_csv(config['data'])
k = config['k-value']
MAX_ITERATIONS = config['MAX-ITERATIONS']
show_plots = config['show-plots']
is_normalized = config['normalize']
initial_indices = config['initial-indices']

# Other Parameters
num_items = len(data)
num_columns = len(data.columns)
currItr = 0
indices = initial_indices if initial_indices is not None else get_random_unique_indices(k, num_items)

# Normalize data - for best result
z_norm = Z_Score_Normalization()

if is_normalized:
    data = z_norm.fit_transform(data)

# scatter plot
if show_plots:
    show_plot(data, data.columns)

# Selecting Initial K Centroids
m = data.iloc[indices, :].reset_index(inplace=False).iloc[:, 1:]

# Class - Clusters
class_dict = {}

while currItr != MAX_ITERATIONS:
    print('{0:5}\t\t\t {1:5}\t\t\t {2:5}'.format("M1", "M2", "Class"))
    print('-------------------------------------')

    # Finishing condition, prev_m
    prev_m = copy.deepcopy(m)

    # distance from each centroid
    classes = [0] * num_items
    SSE = 0
    for index in range(num_items):
        row = data.iloc[index, :]
        distances = []
        for i in range(len(m)):
            distances.append(euclidean_distance(m.iloc[i, :], row))

        # Check which class it belongs to
        class_ = distances.index(min(distances))
        print_table(distances, class_)

        # Add this point to the class
        class_dict[class_] = np.append(class_dict.get(class_, np.array([])), index)
        SSE += distances[class_] ** 2

    # Goodness of cluster
    # Between cluster variation
    BCV = 0
    for i in range(len(m) - 1):
        BCV += euclidean_distance(m.iloc[i, :], m.iloc[i + 1, :])

    BCV_WCV = BCV / SSE
    print('\nBCV / WCV = Between cluster variation / Within Cluster variation = ', round(BCV_WCV, 4))

    # Identifying new centroid
    # For each centroid
    pd.set_option('mode.chained_assignment', None)  # To stop getting warning message of 'CopyWarning'
    print('New Centroid :')
    for i in class_dict.keys():
        m.iloc[i, :] = data.iloc[[int(x) for x in class_dict[i]], :].sum() / len(class_dict[i])
        print('M' + str(i), end=' => ')
        print_table(m.iloc[i, :], None)

    # Breaking Condition
    unchanged_centroids = 0
    if m.equals(prev_m):
        break

    print('======' * 10, '\n\n')
    currItr += 1

# De normalize
if is_normalized:
    data = z_norm.de_normalize(data)

# ik ik .... i need time to get colors
if show_plots:
    colors = ['blue', 'green', 'red', 'orange', 'cyan', 'black', 'pink', 'magenta']
    j = 0
    for x_col, y_col in combinations(range(num_columns), 2):
        plt.subplot(int(math.ceil(nCr(num_columns, 2) / 2.)), 2, j + 1)
        for i in range(len(m)):
            data_ = data.iloc[[int(x) for x in class_dict[i]], :]
            plt.xlabel(data.columns[x_col])
            plt.ylabel(data.columns[y_col])
            plt.scatter(data_.iloc[:, x_col], data_.iloc[:, y_col], c=colors[i])
        j += 1
    plt.show()
