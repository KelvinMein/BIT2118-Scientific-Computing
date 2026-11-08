import numpy as np
import timeit
from scipy.linalg import lu_factor, lu_solve

# Junction balance matrix (same road network every period)
A = np.array([
    [ 6.0, -2.0, -1.0],
    [-2.0,  7.0, -3.0],
    [-1.0, -3.0,  8.0]
])

# Inflow demand in vehicles per minute
periods = {
    "Morning": np.array([30.0, 10.0, 20.0]),
    "Midday":  np.array([20.0, 15.0, 10.0]),
    "Evening": np.array([25.0, 30.0, 35.0])
}

lu, piv = lu_factor(A)

for name, b in periods.items():
    x = lu_solve((lu, piv), b)
    residual = np.linalg.norm(b - A @ x)
    print(f"{name}: flows = {np.round(x, 4)}, residual = {residual:.2e}")

# Compare factor-once against solving from scratch, for 10,000 right-hand sides
rng = np.random.default_rng(0)
B = rng.uniform(10, 40, (10_000, 3))

def solve_each_time():
    for b in B:
        np.linalg.solve(A, b)

def reuse_lu():
    for b in B:
        lu_solve((lu, piv), b)

t1 = timeit.timeit(solve_each_time, number=1)
t2 = timeit.timeit(reuse_lu, number=1)
print(f"Solve from scratch each time: {t1:.4f} s")
print(f"Reuse LU factors:             {t2:.4f} s")