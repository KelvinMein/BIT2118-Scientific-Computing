import numpy as np
from scipy.optimize import root

Ka = 1.8e-5
C = 0.10   # initial concentration in mol/L

# Polynomial: x^2 + Ka*x - Ka*C = 0
roots = np.roots([1, Ka, -Ka * C])
x = roots[roots > 0][0]

# Same equation with a general nonlinear solver
solver = root(lambda v: v**2 / (C - v) - Ka, [0.001])

# Common approximation: ignore x in the denominator
x_approx = np.sqrt(Ka * C)

print("Roots of the polynomial:", roots)
print(f"[H+] from polynomial:  {x:.6e} mol/L")
print(f"[H+] from root():      {solver.x[0]:.6e} mol/L")
print(f"[H+] approximation:    {x_approx:.6e} mol/L")
print(f"pH (exact):            {-np.log10(x):.4f}")
print(f"pH (approximation):    {-np.log10(x_approx):.4f}")
print(f"Percent ionised:       {100 * x / C:.3f} %")
print(f"Approximation error:   {100 * abs(x_approx - x) / x:.3f} %")