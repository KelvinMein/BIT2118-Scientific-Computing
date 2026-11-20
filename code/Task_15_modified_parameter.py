# Modified: step size h varied to study the error of forward and central differences
import numpy as np

# f(x) = sin(x), exact derivative cos(x), evaluated at x = 1
x = 1.0
exact = np.cos(x)

print(f"Exact derivative: {exact:.10f}")
print(f"{'h':>10}{'forward err':>16}{'central err':>16}")
for h in (0.5, 0.1, 0.01, 0.001, 1e-6, 1e-10, 1e-14):
    forward = (np.sin(x + h) - np.sin(x)) / h
    central = (np.sin(x + h) - np.sin(x - h)) / (2 * h)
    print(f"{h:>10.0e}{abs(forward - exact):>16.2e}{abs(central - exact):>16.2e}")