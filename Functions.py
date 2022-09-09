import numpy as np


def gauss_I(X, x0, A, D, T):
    k = np.fix(X / T)
    if k == 0:
        return A * np.exp(-(X - x0) ** 2 / (2 * D)) + A * np.exp(-(X - x0 - T) ** 2 / (2 * D))
    else:
        return A * np.exp(-(X - x0 - T * (k-1))**2 / (2 * D)) + A * np.exp(-(X - x0 - T * k)**2 / (2 * D)) \
               + A * np.exp(-(X - x0 - T * (k + 1))**2 / (2*D))


def pulse_I(t, t0, length, A):
    return 0 if t <= t0 or t >= t0 + length else A
    
    
def pulses_I(t, t01, t02, length, A):
    return A if (t01 <= t <= t01 + length) or (t02 <= t <= t02 + length) else 0


def sin_I(t, t0, length, w, A):
    if t <= t0 or t >= t0+length:
        return 0
    else:
        return np.abs(A*np.sin(w*(t-t0)))
