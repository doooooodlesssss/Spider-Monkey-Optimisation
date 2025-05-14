
import opfunu 

class OPFUNUIntegration:
    def __init__(self, benchmark_name):
        self.benchmark_name = benchmark_name

    def evaluate(self, x):
        # Use the corresponding OPFUNU function for evaluation
        if self.benchmark_name == 'cec2014':
            func = opfunu.cec2014_function()
        elif self.benchmark_name == 'cec2017':
            func = opfunu.cec2017_function()
        elif self.benchmark_name == 'cec2020':
            func = opfunu.cec2020_function()
        elif self.benchmark_name == 'cec2022':
            func = opfunu.cec2022_function()
        return func.evaluate(x)

