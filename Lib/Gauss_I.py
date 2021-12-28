import numpy as np


def gauss_I(X, x0, A, D, T):
    k = np.fix(X / T)
    if k == 0:
        return A * np.exp(-(X - x0) ** 2 / (2 * D)) + A * np.exp(-(X - x0 - T) ** 2 / (2 * D))
    else:
        return A * np.exp(-(X - x0 - T * (k-1))**2 / (2 * D)) + A * np.exp(-(X - x0 - T * k)**2 / (2 * D)) \
               + A * np.exp(-(X - x0 - T * (k + 1))**2 / (2*D))
