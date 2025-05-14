from smo.base_smo import BaseSMO
import numpy as np

class ChaoticSMO(BaseSMO):
    def logistic_map(self, x):
        return 4 * x * (1 - x)

    def initialize_population(self):
        x = np.random.rand()
        pop = []
        for _ in range(self.population_size):
            x = self.logistic_map(x)
            indiv = np.array([b[0] + (b[1] - b[0]) * x for b in self.bounds])
            pop.append(indiv)
        return np.array(pop)

    def optimize(self):
        self.population = self.initialize_population()
        convergence = []

        for eval in range(self.max_evals):
            for i in range(self.population_size):
                chaotic_factor = self.logistic_map(np.random.rand())
                direction = np.random.randn(*self.population[i].shape)
                self.population[i] += chaotic_factor * direction
                self.population[i] = np.clip(self.population[i], [b[0] for b in self.bounds], [b[1] for b in self.bounds])

            current_best = np.min([self.obj_function(ind) for ind in self.population])
            convergence.append(current_best)

        return current_best, convergence
