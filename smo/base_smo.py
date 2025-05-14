import numpy as np

class BaseSMO:
    def __init__(self, obj_function, bounds, max_evals=60000, population_size=30, group_count=3):
        self.obj_function = obj_function
        self.bounds = bounds
        self.dimension = len(bounds)
        self.max_evals = max_evals
        self.population_size = population_size
        self.group_count = group_count
        self.eval_count = 0

        # SMO-specific parameters
        self.local_limit = 5
        self.global_limit = 10

        # Initialize population
        self.population = self.initialize_population()
        self.fitness = np.array([self.evaluate(ind) for ind in self.population])

        self.groups = self.divide_groups()
        self.local_leaders = self.get_local_leaders()
        self.global_leader = self.get_global_leader()
        self.global_limit_counter = 0

    def initialize_population(self):
        return np.array([
            np.array([np.random.uniform(low, high) for (low, high) in self.bounds])
            for _ in range(self.population_size)
        ])

    def evaluate(self, individual):
        self.eval_count += 1
        return self.obj_function(individual)

    def divide_groups(self):
        # Evenly divide population into groups
        return np.array_split(np.arange(self.population_size), self.group_count)

    def get_local_leaders(self):
        local_leaders = []
        for group in self.groups:
            group_fitness = self.fitness[group]
            best_idx = group[np.argmin(group_fitness)]
            local_leaders.append(best_idx)
        return local_leaders

    def get_global_leader(self):
        return np.argmin(self.fitness)

    def update_local_phase(self):
        for g, group in enumerate(self.groups):
            local_leader = self.population[self.local_leaders[g]]
            for i in group:
                if np.random.rand() < 0.5:
                    r = np.random.rand()
                    direction = r * (local_leader - self.population[i])
                    new_pos = self.population[i] + direction
                    new_pos = np.clip(new_pos, [b[0] for b in self.bounds], [b[1] for b in self.bounds])
                    new_fitness = self.evaluate(new_pos)

                    if new_fitness < self.fitness[i]:
                        self.population[i] = new_pos
                        self.fitness[i] = new_fitness

    def update_global_phase(self):
        new_groups = self.divide_groups()
        new_local_leaders = self.get_local_leaders()
        new_global_leader = self.get_global_leader()

        if self.fitness[new_global_leader] >= self.fitness[self.global_leader]:
            self.global_limit_counter += 1
        else:
            self.global_leader = new_global_leader
            self.global_limit_counter = 0

        self.groups = new_groups
        self.local_leaders = new_local_leaders

        # Optional: Reinitialize part of the population if stuck
        if self.global_limit_counter > self.global_limit:
            for i in range(self.population_size):
                if i != self.global_leader:
                    self.population[i] = np.array([np.random.uniform(low, high) for (low, high) in self.bounds])
                    self.fitness[i] = self.evaluate(self.population[i])
            self.global_limit_counter = 0

    def optimize(self):
        convergence_curve = []
        while self.eval_count < self.max_evals:
            self.update_local_phase()
            self.update_global_phase()
            best_fitness = self.fitness[self.global_leader]
            convergence_curve.append(best_fitness)

        return best_fitness, convergence_curve