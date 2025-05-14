import numpy as np

def ABC(obj_func, bounds, colony_size=30, max_iter=1000):
    dim = len(bounds)
    food_sources = bounds[:, 0] + np.random.rand(colony_size, dim) * (bounds[:, 1] - bounds[:, 0])
    fitness = np.array([obj_func(ind) for ind in food_sources])
    trial = np.zeros(colony_size)

    for _ in range(max_iter):
        for i in range(colony_size):
            k = np.random.choice([j for j in range(colony_size) if j != i])
            phi = np.random.uniform(-1, 1, dim)
            new_sol = food_sources[i] + phi * (food_sources[i] - food_sources[k])
            new_sol = np.clip(new_sol, bounds[:, 0], bounds[:, 1])
            new_fit = obj_func(new_sol)
            if new_fit < fitness[i]:
                food_sources[i] = new_sol
                fitness[i] = new_fit
                trial[i] = 0
            else:
                trial[i] += 1

        for i in range(colony_size):
            if trial[i] > 100:
                food_sources[i] = bounds[:, 0] + np.random.rand(dim) * (bounds[:, 1] - bounds[:, 0])
                fitness[i] = obj_func(food_sources[i])
                trial[i] = 0

    best_idx = np.argmin(fitness)
    return food_sources[best_idx], fitness[best_idx]
