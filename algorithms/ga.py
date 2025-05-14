import numpy as np

def GA(obj_func, bounds, population_size=50, generations=1000, mutation_rate=0.01):
    dimension = len(bounds)
    population = np.random.rand(population_size, dimension)
    population = bounds[:, 0] + population * (bounds[:, 1] - bounds[:, 0])
    
    def fitness(ind): return obj_func(ind)

    for generation in range(generations):
        fitness_vals = np.array([fitness(ind) for ind in population])
        best_idx = np.argmin(fitness_vals)
        best_individual = population[best_idx]

        selected = population[np.argsort(fitness_vals)[:population_size//2]]
        offspring = []

        for _ in range(population_size//2):
            parents = selected[np.random.choice(len(selected), 2, replace=False)]
            crossover = np.mean(parents, axis=0)
            if np.random.rand() < mutation_rate:
                mutation = np.random.randn(dimension) * 0.1
                crossover += mutation
            crossover = np.clip(crossover, bounds[:, 0], bounds[:, 1])
            offspring.append(crossover)
        
        population = np.vstack((selected, np.array(offspring)))
    
    return best_individual, fitness(best_individual)
