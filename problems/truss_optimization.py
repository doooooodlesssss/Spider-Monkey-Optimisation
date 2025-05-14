import numpy as np

def truss_structure(x):
    # Simplified 10-bar truss problem
    A = np.array(x)
    L = 100
    E = 1e7
    F = 100000
    constraints = A - 0.1
    penalty = np.sum(np.maximum(0, -constraints)) * 1e6
    weight = L * np.sum(A)
    return weight + penalty
