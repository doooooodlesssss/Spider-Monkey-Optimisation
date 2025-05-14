# evaluations/utils.py

import matplotlib.pyplot as plt
import pandas as pd

def save_convergence_plot(data, filename="convergence_plot.png"):
    plt.plot(data)
    plt.title("Convergence Plot")
    plt.xlabel("Generations")
    plt.ylabel("Fitness Value")
    plt.savefig(filename)

def save_results_to_csv(data, filename="mean_std.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
