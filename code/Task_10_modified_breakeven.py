import numpy as np
from scipy.optimize import root_scalar

def profit(q):
    return 30*q - 0.01*q**2 - 2000

# Profit is negative at q = 0 and positive at q = 500
low = root_scalar(profit, bracket=[0, 500], method="bisect", xtol=1e-8)

# Profit becomes negative again at very high output
high = root_scalar(profit, bracket=[2500, 4000], method="bisect", xtol=1e-8)

# Fixed-point form for the lower break-even: q = (2000 + 0.01*q^2) / 30
def g(q):
    return (2000 + 0.01*q**2) / 30

q = 100.0
for k in range(1, 101):
    q_new = g(q)
    if abs(q_new - q) < 1e-8:
        break
    q = q_new

print(f"Lower break-even (bisection): {low.root:.4f} units")
print(f"Upper break-even (bisection): {high.root:.4f} units")
print(f"Lower break-even (fixed-point): {q_new:.4f} units after {k} iterations")

# Best output between the two break-even points is at the vertex q = 30/(2*0.01)
q_best = 30 / (2 * 0.01)
print(f"Output with maximum profit: {q_best:.0f} units, profit = {profit(q_best):.2f} KES")