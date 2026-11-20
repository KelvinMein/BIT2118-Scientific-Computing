# Task 19: Numerical Optimization

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: cost per unit of 12 (Type A) and 18 (Type B), capacity per unit of 100 and 170, a required total capacity of at least 1000, non-negative allocations, and a starting guess of (5, 3).
Operations: scipy.optimize.minimize with the SLSQP method minimises the cost 12x + 18y subject to the inequality constraint 100x + 170y - 1000 >= 0 and the bounds x, y >= 0. A brute-force search then finds the cheapest whole-server combination.

**Output (code/Task_19_optimization.py):**
```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

## C. Parameter change and effect
Changed the Type B cost from 18 to 25 (code/Task_19_modified_parameter.py).

| | Type B cost 18 | Type B cost 25 |
|---|---|---|
| Cost per capacity, A | 0.120 | 0.120 |
| Cost per capacity, B | 0.106 | 0.147 |
| Optimal allocation | 0 A, 5.882 B | 10 A, 0 B |
| Minimum cost | 105.88 | 120.00 |
| Best whole-server answer | (108, 0, 6, 1020) | (120, 10, 0, 1000) |

With a linear cost and one capacity constraint, the optimum puts everything into the option with the lowest cost per unit of capacity. Raising B's price pushed its cost per capacity (0.147) above A's (0.120), so the solution flipped completely from all B to all A. In the second case 10 A servers give exactly 1000 capacity, so the whole-server answer equals the continuous one, while in the first case rounding up to 6 servers cost an extra 2.12.

## D. Interpretation
The optimiser finds the cheapest way to reach 1000 units of capacity. Type B costs 18/170 = 0.106 per unit of capacity and Type A costs 12/100 = 0.120, so B is cheaper and the optimum uses only B: 1000/170 = 5.882 units at a cost of 105.88. The capacity constraint is exactly met, which is typical because extra capacity only adds cost. Since servers cannot be split, the practical answer is 6 Type B servers, giving capacity 1020 at cost 108. The gap between 105.88 and 108 is the price of using whole servers.

## E. Modified program: least-cost animal feed mix
Code: code/Task_19_modified_feed_mix.py

Assumptions: maize costs 40 KES/kg with 80 g protein and 3.0 energy units per kg; soya costs 90 KES/kg with 400 g protein and 2.5 energy units per kg; the daily need is at least 2000 g protein and 30 energy units.

**Output:**
```
minimize: maize = 7.000 kg, soya = 3.600 kg, cost = 604.00 KES
linprog:  maize = 7.000 kg, soya = 3.600 kg, cost = 604.00 KES
Protein supplied: 2000.0 g, energy supplied: 30.00 units
```

Both solvers agree on 7.000 kg of maize and 3.600 kg of soya at a cost of 604 KES. Protein and energy are both supplied exactly at the minimum, so both constraints are active, and the solution sits at the corner where the two constraint lines meet. By hand, 80m + 400s = 2000 and 3m + 2.5s = 30 give s = 3.6 and m = 7.0. Neither feed alone works: maize alone gives too little protein and soya alone gives too little energy, so the cheapest feed is a blend. Because cost and constraints are linear, linprog is the more suitable tool, and minimize with SLSQP gives the same answer.