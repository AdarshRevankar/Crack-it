import math
from itertools import combinations, permutations
from PIL import ImageDraw, Image, ImagePath


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def __sub__(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def get_tuple(self):
        return self.x * 100, self.y * 100


# Input
N = int(input())
points = []
for _ in range(N):
    x, y = [float(x) for x in input().split()]
    points.append(Point(x, y))


def check(a, b, c, d):
    d2 = a - b
    d3 = a - c
    d4 = a - d
    if d2 == d3 and d4 == math.sqrt(2) * d2:
        if d - b == d - c:
            return True
    return False


# is square
def is_square(p1, p2, p3, p4):
    # Checking condition
    for perm in permutations([p1, p2, p3, p4], 4):
        if check(perm[0], perm[1], perm[2], perm[3]):
            return True
    return False


# Loop combinations
squares = []
for comb in combinations(points, 4):
    if is_square(comb[0], comb[1], comb[2], comb[3]):
        squares.append((comb[0], comb[1], comb[2], comb[3]))

# Plot

from matplotlib import pyplot as plt
if len(squares) > 0:
    for square in squares:
        X = [pt.x for pt in square]
        Y = [pt.y for pt in square]
        plt.fill_between(X, Y)
    plt.show()
