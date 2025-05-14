from smo.base_smo import BaseSMO
import numpy as np

class FuzzySMO(BaseSMO):
    def fuzzy_weight(self, fitness):
        # A simple fuzzy system based on fitness
        if fitness < 1e-2:
            return 0.2
        elif fitness < 1:
            return 0.5
        else:
            return 0.9

    def optimize(self):
        convergence = []

        for eval in range(self.max_evals):
            for i in range(self.population_size):
                fitness = self.obj_function(self.population[i])
                weight = self.fuzzy_weight(fitness)
                direction = np.random.randn(*self.population[i].shape)
                self.population[i] += weight * direction
                self.population[i] = np.clip(self.population[i], [b[0] for b in self.bounds], [b[1] for b in self.bounds])

            current_best = np.min([self.obj_function(ind) for ind in self.population])
            convergence.append(current_best)

        return current_best, convergence
