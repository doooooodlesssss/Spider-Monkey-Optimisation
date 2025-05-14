import numpy as np

def SA(obj_func, bounds, max_iter=1000, temp=1000, cooling_rate=0.95):
    dim = len(bounds)
    current = np.random.rand(dim)
    current = bounds[:, 0] + current * (bounds[:, 1] - bounds[:, 0])
    best = current.copy()
    best_val = obj_func(current)
    
    for _ in range(max_iter):
        candidate = current + np.random.randn(dim) * 0.1
        candidate = np.clip(candidate, bounds[:, 0], bounds[:, 1])
        candidate_val = obj_func(candidate)
        if candidate_val < best_val or np.random.rand() < np.exp((best_val - candidate_val) / temp):
            current = candidate
            if candidate_val < best_val:
                best = candidate
                best_val = candidate_val
        temp *= cooling_rate
    return best, best_val
