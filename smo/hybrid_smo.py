from smo.base_smo import BaseSMO
import numpy as np

class HybridSMO(BaseSMO):
    def optimize(self):
        w, c1, c2 = 0.5, 1.5, 1.5  # PSO-inspired params
        velocity = np.zeros_like(self.population)

        convergence = []

        for eval in range(self.max_evals):
            g_best = self.get_global_best()
            for i in range(self.population_size):
                r1, r2 = np.random.rand(), np.random.rand()
                velocity[i] = w * velocity[i] + c1 * r1 * (g_best - self.population[i])
                self.population[i] += velocity[i]
                self.population[i] = np.clip(self.population[i], [b[0] for b in self.bounds], [b[1] for b in self.bounds])

            current_best = np.min([self.obj_function(ind) for ind in self.population])
            convergence.append(current_best)

        return current_best, convergence
