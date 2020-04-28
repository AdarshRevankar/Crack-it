import math
import pandas as pd
import numpy as np

"""
REFERENCE:
http://www.statskingdom.com/doc_linear_regression.html#multi
"""


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


def form_equation(b):
    b_ = np.reshape(b, (b.shape[0],))
    y = 'Y = ' + str(round(b_[0], 3))
    for i, bi in zip(range(len(b_[1:])), b_[1:]):
        if bi > 0:
            sign = ' +'
        else:
            sign = ' '
        y += sign + str(round(bi, 3)) + ' X' + str(i)
    return y


def compute_equation(x, y):
    y = np.reshape(y, (y.shape[0], 1))

    # Formula to be used
    # B = (X'*X)^-1*X'*Y
    # So we do this step by step

    # 1. X_T = X Transpose
    x_t = np.matrix.transpose(x)

    # 2. (X'*X)^-1
    x_t_x = np.linalg.inv(np.dot(x_t, x))

    # 3. X_T_Y
    h = np.dot(x_t_x, x_t)

    # 4. B computation
    b = np.dot(h, y)

    # 5. y^ is predicted y values
    y_dash = np.dot(x, b)

    # 6. ERROR
    squared_error = ((y - y_dash) ** 2).sum()
    print('Error :', squared_error)

    # B contains the equation
    print(form_equation(b))


# ==============================================
# EXECUTION
# ==============================================

# Load the data
data = pd.read_csv('data.csv', dtype=float)

# Metas
columns = data.columns[:-1]
y_label = data.columns[-1]

# Split
Y = data.iloc[:, -1].to_numpy()

# Compute Co-relation and Greater than threshold
threshold = 0.7
X_matrix = []
for x_label in columns:
    # Obtain best Attributes
    X = data[x_label]
    r = compute_r(X, Y)
    if r >= threshold:
        X_matrix.append(X.to_numpy())

# Convert to numpy array
X_matrix = np.insert(X_matrix, 0, np.ones((1, len(X_matrix[0]))), axis=0)
X_matrix = np.array(X_matrix, dtype=np.float)
X_matrix = np.matrix.transpose(X_matrix)

# X_matrix = np.array([[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 2], [1, 6, 3]])
# Y = np.array([2.1, 3.9, 6.3, 4.95, 7.1, 8.5])

compute_equation(X_matrix, Y)
