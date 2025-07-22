import time
import sys
import random
import pandas as pd
from deterministicQuickSort import deterministic_quicksort
from randomizedQuickSort import randomized_quicksort

# Allow deeper recursion for sorted/reverse inputs
sys.setrecursionlimit(10000)

# Benchmark sttings
sizes = [1000, 2000, 5000]
repeats = 1
distributions = {
        'random':   lambda n: [random.randint(0, n) for _ in range(n)],
        'sorted':   lambda n: list(range(n)),
        'reverse':  lambda n: list(range(n, 0, -1))
    }

results = []

for n in sizes:
    for name, gen in distributions.items():
        # Prepare one input array for randomized tests
        base = gen(n)
        total_rand = 0.0
        for _ in range(repeats):
            arr = base.copy()
            t0 = time.perf_counter()
            randomized_quicksort(arr)
            total_rand += (time.perf_counter() - t0)
        avg_rand = total_rand / repeats

        # Prepare fresh inputs for deterministic tests
        total_det = 0.0
        for _ in range(repeats):
            arr = gen(n)
            t0 = time.perf_counter()
            deterministic_quicksort(arr)
            total_det += (time.perf_counter() - t0)
        avg_det = total_det / repeats

        results.append({
            'n': n,
            'distribution': name,
            'randomized_avg_time_s': avg_rand,
            'deterministic_avg_time_s': avg_det
        })

# Display results
df = pd.DataFrame(results)
print(df)