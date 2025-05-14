import numpy as np

def DE(obj_func, bounds, pop_size=20, generations=1000, F=0.5, CR=0.7):
    dim = len(bounds)
    pop = np.random.rand(pop_size, dim)
    pop = bounds[:, 0] + pop * (bounds[:, 1] - bounds[:, 0])
    fitness = np.array([obj_func(ind) for ind in pop])
    
    for _ in range(generations):
        for i in range(pop_size):
            a, b, c = pop[np.random.choice(np.delete(np.arange(pop_size), i), 3, replace=False)]
            mutant = np.clip(a + F * (b - c), bounds[:, 0], bounds[:, 1])
            cross_points = np.random.rand(dim) < CR
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dim)] = True
            trial = np.where(cross_points, mutant, pop[i])
            f = obj_func(trial)
            if f < fitness[i]:
                pop[i] = trial
                fitness[i] = f
    best_idx = np.argmin(fitness)
    return pop[best_idx], fitness[best_idx]
