# Task 7: Gaussian Elimination and LU Decomposition

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: the 3x3 matrix A = [[4, -1, 0], [-1, 4, -1], [0, -1, 3]] and three measurement vectors b.
Operations: lu_factor factors A once (PA = LU), lu_solve reuses the factors for each b, and the residual b - Ax checks each answer.

**Output (code/Task_07_gaussian_lu.py):**
```
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## C. Parameter change and effect
Changed A[2][2] from 3.0 to 5.0 (code/Task_07_modified_parameter.py).

| | Original (A[2][2] = 3) | Modified (A[2][2] = 5) |
|---|---|---|
| Set 1 | [5, 5, 5] | [4.859, 4.437, 2.887] |
| Set 2 | [5.317, 5.268, 4.756] | [5.183, 4.732, 2.746] |
| Set 3 | [4.902, 5.610, 5.537] | [4.746, 4.986, 3.197] |
| Residual norms | 0 to 1.8e-15 | 0 to 1.8e-15 |

Changing one entry of A changed all three unknowns in every measurement set, not only z, because the equations are coupled: a change in the third equation passes through y to x. The value of z fell the most (from 5 to 2.89 in set 1), because the third equation became -y + 5z = 10, so a smaller z is enough to balance it. By hand, set 1 gives x = 345/71 = 4.859, y = 4.437 and z = 2.887, which matches the program. The old L and U factors belong to the old matrix, so A had to be factored again. The residuals stayed near 1e-15, so the new solutions are still accurate.

## D. Interpretation
LU decomposition writes the matrix as PA = LU, where L is lower triangular, U is upper triangular and P records row swaps. Solving Ax = b then becomes two cheap steps: forward substitution with L, then back substitution with U. For set 1 the answer