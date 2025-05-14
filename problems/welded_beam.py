import numpy as np

def welded_beam(x):
    h, l, t, b = x
    P = 6000
    L = 14
    E = 30e6
    G = 12e6
    tau_max = 13600
    sigma_max = 30000
    delta_max = 0.25

    M = P * (L + l / 2)
    R = np.sqrt((l**2 / 4) + ((h + t) / 2)**2)
    J = 2 * (np.sqrt(2) * h * l * (l**2 / 12 + ((h + t) / 2)**2))
    tau_prime = P / (np.sqrt(2) * h * l)
    tau_double_prime = M * R / J
    tau = np.sqrt(tau_prime**2 + 2*tau_prime*tau_double_prime*l / (2*R) + tau_double_prime**2)
    sigma = 6 * P * L / (b * t**2)
    delta = 4 * P * L**3 / (E * b * t**3)

    cost = 1.10471 * h**2 * l + 0.04811 * t * b * (14 + l)
    penalty = 0
    penalty += max(0, tau - tau_max)
    penalty += max(0, sigma - sigma_max)
    penalty += max(0, delta - delta_max)
    penalty += max(0, h - b)
    return cost + 1e6 * penalty
