import pandas as pd
from matplotlib import pyplot as plt
import math

'''
Author  : Adarsh Revankar
Date    : 19-04-2020
Purpose : Computing best model for the given data
'''


# ========================================================
# HELPER FUNCTIONS
# ========================================================
def compute_r(x, y):
    """
    Computes the Coefficient of Co-relation using Pearson's method
    """
    n = len(x)
    numerator = n * ((x * y).sum()) - (x.sum() * y.sum())
    denominator = (n * (x ** 2).sum()) - x.sum() ** 2
    denominator *= (n * (y ** 2).sum()) - y.sum() ** 2
    denominator = math.sqrt(denominator)
    return numerator / denominator


# ========================================================
# EXECUTION
# ========================================================
# Load the data
data = pd.read_csv('data.csv', dtype=float)

# Split
Y = data.iloc[:, -1]
columns = data.columns[:-1]
y_label = data.columns[-1]

# Parameters
threshold = 0.7
N_attribs = len(columns)

for i, x_label in zip(range(N_attribs), columns):
    # X Data
    X = data[x_label]

    # Compute Coefficient of Co-relation
    r = compute_r(X, Y)

    # Find Slope & Intercept
    slope = (Y.std() / X.std()) * r
    intercept = Y.mean() - slope * X.mean()

    # Check if 'r' is within the threshold
    if r < threshold:
        continue

    print(f'\nLinear Equation: {x_label} vs {y_label}')
    print(f'Coefficient of Co-relation :{round(r, 2)}')
    print(f'Coefficient of Co-relation r^2:{round(r ** 2, 2)}')
    if intercept >= 0:
        print(f'  Y = {round(slope, 2)} * X + {round(intercept, 2)}')
    else:
        print(f'  Y = {round(slope, 2)} * X {round(intercept, 2)}')

    # Plot
    plt.subplot(int(math.ceil(N_attribs / 2)), 2, i + 1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plot_x = pd.Series([x for x in range(int(X.min() - 5), int(X.max() + 5))])
    plot_y = slope * plot_x + intercept
    plt.plot(plot_x, plot_y, c='red')
    plt.scatter(X, Y, c='blue', alpha=0.5)

plt.show()
