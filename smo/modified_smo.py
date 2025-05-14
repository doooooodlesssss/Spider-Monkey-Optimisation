from smo.base_smo import BaseSMO
import numpy as np

class ModifiedSMO(BaseSMO):
    def optimize(self):
        convergence = []

        for eval in range(self.max_evals):
            for i in range(self.population_size):
                # Modified position update: use neighborhood-based update
                r1, r2 = np.random.choice(self.population, 2, replace=False)
                new_pos = self.population[i] + 0.5 * (r1 - r2)

                # Clamp
                new_pos = np.clip(new_pos, [b[0] for b in self.bounds], [b[1] for b in self.bounds])
                self.population[i] = new_pos

            current_best = np.min([self.obj_function(ind) for ind in self.population])
            convergence.append(current_best)

        return current_best, convergence
