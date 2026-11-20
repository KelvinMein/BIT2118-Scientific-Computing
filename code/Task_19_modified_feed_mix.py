import numpy as np
from scipy.optimize import minimize, linprog

cost_per_kg = np.array([40.0, 90.0])      # maize, soya
protein = np.array([80.0, 400.0])         # g per kg
energy = np.array([3.0, 2.5])             # units per kg

min_protein, min_energy = 2000.0, 30.0

# Method 1: minimize with inequality constraints
cons = [
    {"type": "ineq", "fun": lambda z: protein @ z - min_protein},
    {"type": "ineq", "fun": lambda z: energy @ z - min_energy},
]
res = minimize(lambda z: cost_per_kg @ z, x0=[10, 5], method="SLSQP",
               bounds=[(0, None), (0, None)], constraints=cons)

# Method 2: linear programming (constraints written as A_ub z <= b_ub)
lp = linprog(cost_per_kg,
             A_ub=-np.array([protein, energy]),
             b_ub=-np.array([min_protein, min_energy]),
             bounds=[(0, None), (0, None)])

print("minimize: maize = %.3f kg, soya = %.3f kg, cost = %.2f KES" % (res.x[0], res.x[1], res.fun))
print("linprog:  maize = %.3f kg, soya = %.3f kg, cost = %.2f KES" % (lp.x[0], lp.x[1], lp.fun))
print("Protein supplied: %.1f g, energy supplied: %.2f units" % (protein @ lp.x, energy @ lp.x))