import numpy as np

def speed_reducer(x):
    x1, x2, x3, x4, x5, x6, x7 = x
    f = 0.7854*x1*x2**2*(3.3333*x3**2 + 14.9334*x3 - 43.0934)
    f -= 1.508*x1*(x6**2 + x7**2)
    f += 7.4777*(x6**3 + x7**3)
    f += 0.7854*(x4*x6**2 + x5*x7**2)
    return f
