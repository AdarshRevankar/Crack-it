import copy
import math
import random
from functools import lru_cache
from itertools import combinations

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ===========================================================
# HELPING FUNCTIONS
# ===========================================================
@lru_cache(maxsize=1000)
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


def show_plot(data, columns, clr='red', show=True):
    num_rows = int(math.ceil(nCr(len(columns), 2) / 2.))
    subplot_index = 1
    for x_label, y_label in combinations(columns, 2):
        plt.subplot(num_rows, 2, subplot_index)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.scatter(data[x_label], data[y_label], c=clr)
        subplot_index += 1
    if show:
        plt.show()


def euclidean_distance(point1, point2):
    # Distance between 2 data points
    return (((point1 - point2) ** 2).sum()) ** 0.5


def get_random_unique_indices(k, out_bound):
    ind = []
    while len(ind) != k:
        item = random.randint(0, out_bound - 1)
        if item not in ind:
            ind.append(item)
    return ind


def print_table(distances, cls_):
    for d in distances:
        print("{0:7.2f}".format(d), end=' ')
    print(cls_ if cls_ is not None else ' ')


# ===========================================================
# EXECUTION
# ===========================================================
# Data
data = pd.read_csv('Shirt_Cluster.csv', dtype=float)
num_items = len(data)
num_columns = len(data.columns)

# K value
k = 2

# scatter plot
show_plot(data, data.columns)

# Selecting Initial K Centroids
indices = get_random_unique_indices(k, num_items)
# indices = [6, 7]
m = data.iloc[indices, :]

while True:
    # Finishing condition, prev_m
    prev_m = copy.deepcopy(m)

    # distance from each centroid
    classes = [0] * num_items
    class_dict = {}
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
    for i in range(len(m)):
        m.iloc[i, :] = data.iloc[[int(x) for x in class_dict[i]], :].sum() / len(class_dict[i])
        print('M' + str(i), end=' => ')
        print_table(m.iloc[i, :], None)

    # Breaking Condition
    unchanged_centroids = 0
    if m.equals(prev_m):
        break

    print('\n', '======' * 10, '\n\n')

# ik ik .... i need time to get colors
colors = ['blue', 'green', 'red', 'orange', 'cyan', 'black', 'pink', 'magenta']
for x_col, y_col in combinations(range(len(data.columns)), 2):
    for i in range(len(m)):
        data_ = data.iloc[[int(x) for x in class_dict[i]], :]
        plt.xlabel(data.columns[x_col])
        plt.ylabel(data.columns[y_col])
        plt.scatter(data_.iloc[:, x_col], data_.iloc[:, y_col], c=colors[i])
    # plt.savefig('C:/image.png')
    plt.show()
