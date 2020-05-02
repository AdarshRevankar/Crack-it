import math
import random
from functools import lru_cache
from itertools import combinations

from matplotlib import pyplot as plt


class Z_Score_Normalization:
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, x):
        self.mean = x.mean(axis=0)
        self.std = x.std(axis=0)

    def transform(self, x):
        if self.mean is not None and self.std is not None:
            return (x - self.mean) / self.std
        else:
            raise RuntimeError('Please do fit the Normalization layer then do transform or use fit_transform')

    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)

    def de_normalize(self, x):
        return self.std * x + self.mean


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


def get_random_unique_indices(k, out_bound):
    ind = []
    while len(ind) != k:
        item = random.randint(0, out_bound - 1)
        if item not in ind:
            ind.append(item)
    return ind


def print_table(dist, cls_):
    for d in dist:
        print("{0:5.2f}\t\t\t".format(d), end=' ')
    if cls_ is not None:
        print(f'M{cls_}')
    else:
        print()
