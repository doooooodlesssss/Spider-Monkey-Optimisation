# cec_benchmarks/cec2022.py

from opfunu import OPFUNUIntegration

def run_cec2022_benchmark():
    opfunu = OPFUNUIntegration('cec2022')

    # Example: Evaluate a sample solution
    x = [0.5, -0.3, 0.1, 0.7]  # Sample solution
    result = opfunu.evaluate(x)
    print(f"CEC 2022 Benchmark Result: {result}")

# Call this function in your main script
