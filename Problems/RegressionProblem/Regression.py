import pandas as pd
from matplotlib import pyplot as plt
import math

'''
Author  : Adarsh Revankar
Date    : 19-04-2020
Purpose : Computing best model for the given data
'''

# Load the data
data = pd.read_csv('data.csv', dtype=float)

# Split
Y = data.iloc[:, -1]
columns = data.columns[:-1]
y_label = data.columns[-1]


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


best_r = None
best_r_label = None

# Select the best attribute
slopes_ = []
intercepts_ = []
threshold = 0.7
N_attribs = len(columns)

for i, x_label in zip(range(N_attribs), columns):
    X = data[x_label]
    r = compute_r(X, Y)

    slope = (Y.std() / X.std()) * r
    intercept = Y.mean() - slope * X.mean()

    if r >= threshold:
        slopes_.append(slope)
        intercepts_.append(intercept)

    print(f'\nLinear Equation: {x_label} vs {y_label}')
    print(f'Coefficient of Co-relation :{round(r, 2)}')
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

'''
=======================
MULTI LINEAR REGRESSION
=======================
Since,
y = A1 * x + B1
y = A2 * x + B2
y = A3 * x + B3
...

we just add all the equations
N * y = [ A1 + A2 + ... + AN ] * x + [ B1 + B2 + ... + BN ]
y = [ A1 + A2 + ... + AN ]/N * x + [ B1 + B2 + ... + BN ]/N
=======================
'''
print('\n', '====' * 10)
print(f'Multiple Linear Regression')
equation = ' Y = '
for i, s in zip(range(len(slopes_)), slopes_):
    equation += ' ' + str(round(s / len(slopes_), 2)) + ' * X' + str(i) + ' +'
equation += ' ( ' + str(round(sum(intercepts_) / len(slopes_))) + ' )'
print(equation)
