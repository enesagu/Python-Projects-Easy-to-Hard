import numpy as np
import timeit
from numba import jit

# Define a Python function that calculates the sum of squares
def sum_of_squares(arr):
    result = 0
    for x in arr:
        result += x**2
    return result

# Decorate the function with @jit to compile it with Numba
@jit
def numba_sum_of_squares(arr):
    result = 0
    for x in arr:
        result += x**2
    return result

# Create a large array
arr = np.arange(1000000)

# Time the execution of the Python function
start_time = timeit.default_timer()
sum_of_squares(arr)
end_time = timeit.default_timer()
python_time = end_time - start_time

# Time the execution of the Numba-compiled function
start_time = timeit.default_timer()
numba_sum_of_squares(arr)
end_time = timeit.default_timer()
numba_time = end_time - start_time

print("Python Function Execution Time:", python_time)
print("Numba-compiled Function Execution Time:", numba_time)