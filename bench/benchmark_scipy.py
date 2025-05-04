#!/usr/bin/env python3
# benchmark_scipy.py
import math
import time

from scipy.optimize import minimize


def rosenbrock(x):
    """Rosenbrock function - a classical test case for optimization"""
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def quadratic(x):
    """Simple quadratic function: f(x) = x[0]^2 + x[1]^2"""
    return x[0] ** 2 + x[1] ** 2


def sum_squares(x):
    """Sum of squares function: f(x) = x[0]^2 + x[1]^2 + ... + x[n-1]^2"""
    return sum(xi**2 for xi in x)


# Test with Rosenbrock function
print("\n=== Powell's Method (SciPy) - Rosenbrock Function ===")
x0 = [0.0, 0.0]
start_time = time.time()
result = minimize(rosenbrock, x0, method="Powell")
end_time = time.time()

print(f"Solution: {result.x}")
print(f"Function value: {result.fun}")
print(f"Number of iterations: {result.nit}")
print(f"Success: {result.success}")
print(f"Execution time: {end_time - start_time:.4f} seconds")

# Verify solution
assert math.isclose(
    result.fun, 0.0, abs_tol=1e-4
), "Function minimum should be close to 0"
assert math.isclose(result.x[0], 1.0, abs_tol=1e-2), "x[0] should be close to 1"
assert math.isclose(result.x[1], 1.0, abs_tol=1e-2), "x[1] should be close to 1"

# Test with quadratic function
print("\n=== Powell's Method (SciPy) - Quadratic Function ===")
x0 = [1.0, 1.0]
start_time = time.time()
result = minimize(quadratic, x0, method="Powell")
end_time = time.time()

print(f"Solution: {result.x}")
print(f"Function value: {result.fun}")
print(f"Number of iterations: {result.nit}")
print(f"Success: {result.success}")
print(f"Execution time: {end_time - start_time:.4f} seconds")

# Verify solution
assert math.isclose(
    result.fun, 0.0, abs_tol=1e-4
), "Function minimum should be close to 0"
assert math.isclose(result.x[0], 0.0, abs_tol=1e-2), "x[0] should be close to 0"
assert math.isclose(result.x[1], 0.0, abs_tol=1e-2), "x[1] should be close to 0"

# Test with sum_squares function (10D)
print("\n=== Powell's Method (SciPy) - Sum Squares (10D) ===")
x0 = [1.0] * 10
start_time = time.time()
result = minimize(sum_squares, x0, method="Powell")
end_time = time.time()

print(f"Solution: {result.x}")
print(f"Function value: {result.fun}")
print(f"Number of iterations: {result.nit}")
print(f"Success: {result.success}")
print(f"Execution time: {end_time - start_time:.4f} seconds")

# Verify solution
assert math.isclose(
    result.fun, 0.0, abs_tol=1e-4
), "Function minimum should be close to 0"
for i in range(10):
    assert math.isclose(result.x[i], 0.0, abs_tol=1e-2), f"x[{i}] should be close to 0"

print("\nAll tests passed!")
