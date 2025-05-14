import numpy as np

# Original PSO function
def run_pso(obj_func, bounds, num_particles=30, max_iter=1000, w=0.5, c1=1.5, c2=1.5):
    dim = len(bounds)
    pos = np.random.rand(num_particles, dim)
    pos = bounds[:, 0] + pos * (bounds[:, 1] - bounds[:, 0])
    vel = np.zeros_like(pos)
    personal_best = pos.copy()
    personal_best_val = np.array([obj_func(p) for p in pos])
    global_best = personal_best[np.argmin(personal_best_val)]
    global_best_val = personal_best_val[np.argmin(personal_best_val)]

    convergence_curve = []

    for _ in range(max_iter):
        r1, r2 = np.random.rand(), np.random.rand()
        vel = w * vel + c1 * r1 * (personal_best - pos) + c2 * r2 * (global_best - pos)
        pos += vel
        pos = np.clip(pos, bounds[:, 0], bounds[:, 1])
        scores = np.array([obj_func(p) for p in pos])
        for i in range(num_particles):
            if scores[i] < personal_best_val[i]:
                personal_best[i] = pos[i]
                personal_best_val[i] = scores[i]
        best_index = np.argmin(personal_best_val)
        global_best = personal_best[best_index]
        global_best_val = personal_best_val[best_index]

        convergence_curve.append(global_best_val)

    return global_best_val, convergence_curve


# Wrapper function to match the expected interface
def PSO(problem, num_evals):
    return run_pso(problem['obj_func'], np.array(problem['bounds']), max_iter=num_evals // 30)
