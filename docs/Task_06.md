# Task 6: Solution of Systems of Linear Equations

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: matrix A = [[4, 2], [8, 12]] and vector b = [20, 72].
Operations: solve Ax = b with np.linalg.solve, verify with A @ x, and compute the residual b - Ax.

**Output (code/Task_06_linear_systems.py):**
```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## C. Parameter change and effect
Changed the memory total from 72 GB to 80 GB (code/Task_06_modified_parameter.py).

| | Original | Modified |
|---|---|---|
| b (CPU, memory) | [20, 72] | [20, 80] |
| Type A servers | 3 | 2.50 |
| Type B servers | 4 | 5.00 |
| Residual norm | 0.0 | 0.0 |

Raising the memory total by 8 GB moved the solution from (3, 4) to (2.5, 5). Type B uses more memory per server than Type A (12 GB against 8 GB), so more memory with the same CPU total is explained by fewer Type A servers and more Type B servers. The matrix A did not change, and det(A) = 4 x 12 - 2 x 8 = 32, which is not zero, so a unique solution exists for any values of b. The residual stayed at 0, so the new solution satisfies both equations. However, 2.5 servers is not physically possible, so these observed totals cannot come from whole servers. In practice this would point to a measurement error or a third server type.

## D. Interpretation
Each row of the system is one resource balance: the first row says 4x + 2y = 20 CPU units and the second says 8x + 12y = 72 GB of memory. Solving the system gives 3 Type A servers and 4 Type B servers, and the check is direct: 4(3) + 2(4) = 20 and 8(3) + 12(4) = 72. The verification A @ solution reproduces b exactly, and the residual norm of 0.0 shows that the solution satisfies both equations with no visible round-off error. Because det(A) is not zero, the two equations are independent and only one combination of servers fits the observed usage. np.linalg.solve is preferred to computing the inverse of A because it is faster and more accurate.

## E. Modified program: three-loop circuit
Code: code/Task_06_modified_circuit.py

Assumptions: mesh currents from Kirchhoff's voltage law; 12 V source in loop 1, a 6 V source opposing in loop 3; resistances as in the matrix (ohms).

**Output:**
```
Determinant of A: 590.0
Condition number: 2.55
I1 = 1.1797 A
I2 = 0.2644 A
I3 = -0.2441 A
Verification A @ I: [ 1.20000000e+01  2.22044605e-16 -6.00000000e+00]
Residual norm: 9.155133597044475e-16
```

Each equation is Kirchhoff's voltage law for one loop, so the three equations are solved together to find the three mesh currents. The determinant is 590, which is not zero, so the circuit has a unique solution. The condition number of 2.55 is small, which means the answer is not sensitive to small errors in the resistances or voltages. I1 = 1.1797 A is positive, so loop 1 current flows in the assumed direction, driven by the 12 V source. I3 = -0.2441 A is negative, which means that current flows opposite to the assumed direction, because the opposing 6 V source dominates loop 3. The verification line reproduces b = [12, 0, -6], where the 2.2e-16 stands in for 0 as floating-point round-off. The residual norm of about 9e-16 is close to machine precision, so the solution satisfies all three equations.