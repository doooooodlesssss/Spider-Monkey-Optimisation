# cec_benchmarks/cec2014.py

from opfunu import OPFUNUIntegration

def run_cec2014_benchmark():
    opfunu = OPFUNUIntegration('cec2014')

    # Example: Evaluate a sample solution
    x = [0.5, -0.3, 0.1, 0.7]  # Sample solution
    result = opfunu.evaluate(x)
    print(f"CEC 2014 Benchmark Result: {result}")

# Call this function in your main script
