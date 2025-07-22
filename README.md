# QuickSort

This repository provides two Python implementations of the QuickSort algorithm—**deterministic** and **randomized**—together with a small benchmarking script to compare their performance on different input distributions.

## Repository Structure

- **`deterministicQuickSort.py`**  
  A simple, functional QuickSort that always picks the first element of the array as the pivot. Returns a newly sorted list via list comprehensions.

- **`randomizedQuickSort.py`**  
  A variant of QuickSort that selects its pivot uniformly at random from the array on each recursive call, in order to avoid consistently unbalanced partitions on certain inputs.

- **`benchmark.py`**  
  A script that measures and compares the average running times of the deterministic and randomized implementations on three kinds of input arrays (random, already sorted, and reverse‐sorted) across multiple sizes (e.g., 1 000, 2 000, and 5 000 elements).

- **`.gitignore`**  
  Standard Python ignores (e.g., `__pycache__/`, etc.).

## Requirements

- Python 3.6 or higher  
- (No external dependencies—all code uses only the Python standard library.)

## Usage

1. **Clone the repository**  
    ```bash
    git clone https://github.com/leminh646/QuickSort
    cd QuickSort
    ```

2. **Run the benchmark**
    ```bash
    python benchmark.py
    ```
    This will generate timing results for both implementations and print them in a tabular format, for example:

            n distribution  randomized_avg_time_s  deterministic_avg_time_s
        0  1000       random               0.002531                  0.002154
        1  1000       sorted               0.002569                  0.076618
        2  1000      reverse               0.002750                  0.076462
        3  2000       random               0.005875                  0.004684
        4  2000       sorted               0.005303                  0.293152
        5  2000      reverse               0.006019                  0.302336
        6  5000       random               0.014418                  0.013739
        7  5000       sorted               0.015196                  1.848416
        8  5000      reverse               0.017591                  1.905342

3. **Inspect or modify**
    - To change the array sizes, input distributions, or number of trials, open and edit benchmark.py.
    - To adapt pivot‑selection behavior or in‑place sorting, modify the respective *.py file.

    Both implementations run in Θ(n log n) on average; the deterministic variant can fall back to Θ(n²) on already sorted or reverse‑sorted arrays, whereas the randomized version remains O(n log n) in expectation on all inputs.