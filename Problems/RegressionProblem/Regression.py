import pandas as pd
import math
import matplotlib.pyplot as plt

'''
Author  : Adarsh Revankar
Date    : 19-04-2020
Purpose : Computing best model for the given data
'''

# Load the data
data = pd.read_excel('data.xlsx', dtype=float)

# Split
Y = data.iloc[:, -1]
columns = data.columns


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
for x_label in columns[:-1]:
    X = data[x_label]
    r = compute_r(X, Y)
    if best_r is None:
        best_r = r
        best_r_label = x_label
    elif best_r < r:
        best_r = r
        best_r_label = x_label
    print(f'r({x_label}) = {r}')

print(f'\nBest r is "{best_r_label}" with r = {best_r}')

# Forming the Model
X = data[best_r_label]

slope = (Y.std() / X.std()) * best_r
intercept = Y.mean() - slope * X.mean()

print(f'\nBest fitted model using linear equation is: ')
if intercept >= 0:
    print(f'  Y = {slope} * X + {intercept}')
else:
    print(f'  Y = {slope} * X {intercept}')

# Plotting
plot_x = pd.Series([x for x in range(int(X.min() - 5), int(X.max() + 5))])
plot_y = slope * plot_x + intercept

plt.plot(plot_x, plot_y, c='red')
plt.scatter(X, Y, c='blue')
plt.show()
