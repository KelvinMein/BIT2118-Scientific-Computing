# Task 12: Polynomial and Nonlinear Equation Solving

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: a circle x^2 + y^2 = 4 and a parabola y = x^2 - 1, written as two residual equations, with starting guesses (1, 1) and (-1, 1).
Operations: scipy.optimize.root searches for (x, y) that make both residuals zero. Each result is checked by printing the residuals.

**Output (code/Task_12_nonlinear_equations.py):**
```
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [-2.4780177909633494e-13, -2.4158453015843406e-13]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [-2.4780177909633494e-13, -2.4158453015843406e-13]
Converged: True
```

## C. Parameter change and effect
Changed the circle from x^2 + y^2 = 4 to x^2 + y^2 = 9 (code/Task_12_modified_parameter.py).

| | Circle radius squared 4 | Circle radius squared 9 |
|---|---|---|
| Right intersection | (1.5175, 1.3028) | (1.8364, 2.3723) |
| Left intersection | (-1.5175, 1.3028) | (-1.8364, 2.3723) |
| Residuals | about 2.4e-13 | about 1.4e-12 |

A larger circle moved both intersections up and outward. They remain mirror images because both curves are symmetric about the y-axis. By hand, substituting x^2 = y + 1 gives y^2 + y - 8 = 0, so y = (-1 + sqrt(33))/2 = 2.3723 and x = +/- sqrt(3.3723) = +/- 1.8364, which matches the solver.

## D. Interpretation
Each intersection is a point that lies on both curves at once, so it satisfies both equations. By hand for the first case, x^2 = y + 1 gives y^2 + y - 3 = 0, so y = (-1 + sqrt(13))/2 = 1.3028 and x = +/- 1.5175. The other root, y = -2.3028, is rejected because it would need x^2 = -1.3028, which has no real solution. The two starting guesses found the two different intersections, which shows that a nonlinear solver finds the root nearest to its starting point, so several guesses are needed to find all the solutions. Residuals of about 1e-13 show that both equations are satisfied up to round-off, and Converged: True confirms the solver succeeded.

## E. Modified program: weak-acid equilibrium
Code: code/Task_12_modified_acid_equilibrium.py

Assumptions: acetic acid with initial concentration 0.10 mol/L and Ka = 1.8e-5; the hydrogen ion concentration x satisfies x^2 / (0.10 - x) = Ka, which rearranges to the polynomial x^2 + Ka x - Ka(0.10) = 0.

**Output:**
```
Roots of the polynomial: [-0.00135067  0.00133267]
[H+] from polynomial:  1.332671e-03 mol/L
[H+] from root():      1.332671e-03 mol/L
[H+] approximation:    1.341641e-03 mol/L
pH (exact):            2.8753
pH (approximation):    2.8724
Percent ionised:       1.333 %
Approximation error:   0.673 %
```

The polynomial has two roots, and only the positive one, 1.3327e-3 mol/L, is physical, because a concentration cannot be negative. The general solver root() gave the same value, so the two methods agree. The pH is 2.8753, and about 1.33% of the acid is ionised. The common shortcut, x = sqrt(Ka x C), ignores x in the denominator and gives 1.3416e-3 mol/L, an error of only 0.67%, because the acid is weak. For a stronger or more dilute acid, a larger fraction ionises and the shortcut becomes less accurate, so the full polynomial should be used.