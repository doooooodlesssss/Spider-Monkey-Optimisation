import numpy as np
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon
from statistics import mean, stdev
# from algorithms import ga, pso, aco, sa, de, abc 
from algorithms.ga import GA
from algorithms.pso import PSO
from algorithms.aco import ACO
from algorithms.sa import SA
from algorithms.de import DE
from algorithms.abc import ABC
from smo import base_smo, adaptive_smo, modified_smo, hybrid_smo, fuzzy_smo, chaotic_smo, final_smo
from problems import pressure_vessel, speed_reducer, welded_beam, truss_optimization  
# evaluations/run_benchmark.py



# Functions to evaluate each engineering problem
def evaluate_problem(problem, algorithm, num_runs=50, num_evals=60000):
    best_results = []
    convergence_curves = []
    
    for run in range(num_runs):
        start_time = time.time()
        best_result, convergence_curve = algorithm(problem, num_evals)
        elapsed_time = time.time() - start_time
        best_results.append(best_result)
        convergence_curves.append(convergence_curve)
    
    # Calculate mean and std
    mean_result = mean(best_results)
    std_result = stdev(best_results)
    
    return mean_result, std_result, convergence_curves

algorithms = {
    "GA": GA,
    "PSO": PSO,
    "ACO": ACO,
    "SA": SA,
    "DE": DE,
    "ABC": ABC,
    "SMO": base_smo,
    "Modified SMO": modified_smo,
    "Hybrid SMO": hybrid_smo,
    "Fuzzy SMO": fuzzy_smo,
    "Chaotic SMO": chaotic_smo,
}


# List of all engineering problems
problems = {
    "Pressure Vessel": pressure_vessel,
    "Speed Reducer": speed_reducer,
    "Welded Beam": welded_beam,
    "Truss Structure": truss_optimization,
}

# Function to plot convergence curve
def plot_convergence_curve(convergence_curves, algorithm_name, problem_name):
    plt.figure(figsize=(10, 6))
    for curve in convergence_curves:
        plt.plot(curve)
    plt.title(f'Convergence Curve - {algorithm_name} on {problem_name}')
    plt.xlabel('Evaluations')
    plt.ylabel('Best Solution')
    plt.grid(True)
    plt.savefig(f'./results/{algorithm_name}_{problem_name}_convergence.png')
    plt.close()

# Run the benchmarking for all algorithms and problems
def run_benchmark():
    os.makedirs('./results', exist_ok=True)
    
    results = []
    
    # Iterate through all problems and algorithms
    for problem_name, problem in problems.items():
        for algorithm_name, algorithm in algorithms.items():
            print(f"Running {algorithm_name} on {problem_name}...")
            
            # Evaluate the problem using the algorithm
            mean_result, std_result, convergence_curves = evaluate_problem(problem, algorithm)
            
            # Save the convergence plot
            plot_convergence_curve(convergence_curves, algorithm_name, problem_name)
            
            # Save the results for this run
            results.append({
                "Problem": problem_name,
                "Algorithm": algorithm_name,
                "Mean": mean_result,
                "Standard Deviation": std_result
            })
    
    # Save results as a CSV file
    df = pd.DataFrame(results)
    df.to_csv('./results/benchmark_results.csv', index=False)
    
    print("Benchmarking complete. Results saved.")

# Statistical Tests: Wilcoxon
def perform_wilcoxon_test(results):
    print("Performing Wilcoxon Tests...")
    all_algorithms = list(set(result['Algorithm'] for result in results))
    
    for algorithm1 in all_algorithms:
        for algorithm2 in all_algorithms:
            if algorithm1 != algorithm2:
                algorithm1_results = [result['Mean'] for result in results if result['Algorithm'] == algorithm1]
                algorithm2_results = [result['Mean'] for result in results if result['Algorithm'] == algorithm2]
                
                stat, p_value = wilcoxon(algorithm1_results, algorithm2_results)
                print(f"Wilcoxon Test between {algorithm1} and {algorithm2}: p-value = {p_value}")

if __name__ == "__main__":
    # Run the benchmarking process
    run_benchmark()

    # Load the results from CSV
    results_df = pd.read_csv('./results/benchmark_results.csv')
    
    # Perform statistical tests (Wilcoxon test)
    perform_wilcoxon_test(results_df)
    



