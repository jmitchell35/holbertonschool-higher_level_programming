import timeit
import random

# Create a test list with random integers
test_list = [random.randint(1, 1000) for _ in range(10000)]

# Setup for timeit
setup = "from __main__ import test_list"

# Define the methods to test
methods = {
    "Slicing": "new_list = test_list[:]",
    "List constructor": "new_list = list(test_list)",
    "List comprehension": "new_list = [x for x in test_list]",
    "For loop with append": """
new_list = []
for item in test_list:
    new_list.append(item)
"""
}

# Run benchmarks
results = {}
iterations = 10000

print(f"Benchmarking list cloning methods with a list of {len(test_list)} elements:")
print("-" * 60)

for name, code in methods.items():
    time = timeit.timeit(stmt=code, setup=setup, number=iterations)
    results[name] = time
    print(f"{name}: {time:.6f} seconds for {iterations} iterations")

# Find the fastest method
fastest = min(results, key=results.get)
print("-" * 60)
print(f"Fastest method: {fastest}")

# Compare relative performance
print("\nRelative performance (fastest method = 1.0):")
fastest_time = results[fastest]
for name, time in sorted(results.items(), key=lambda x: x[1]):
    print(f"{name}: {time/fastest_time:.2f}x")
