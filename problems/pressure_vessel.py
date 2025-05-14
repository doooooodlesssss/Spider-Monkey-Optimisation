import numpy as np

def pressure_vessel(x):
    x1, x2, x3, x4 = x
    cost = 0.6224*x1*x3*x4 + 1.7781*x2*x3**2 + 3.1661*x1**2*x4 + 19.84*x1**2*x3
    penalty = 0
    penalty += max(0, 0.0193*x3 - x1)
    penalty += max(0, 0.00954*x3 - x2)
    penalty += max(0, np.pi*x3**2*x4 + (4/3)*np.pi*x3**3 - 1296000)
    return cost + 1e6 * penalty
