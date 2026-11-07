# Task 4: Floating-Point Arithmetic and Numerical Errors

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: 0.1, 0.2, 0.3; sqrt(2) vs 1.414; x = 1e-4, 1e-8, 1e-12.
Operations: exact vs tolerance comparison, absolute error |true - approx|, relative error = absolute / |true|, and the unstable (sqrt(1+x)-1)/x vs stable 1/(sqrt(1+x)+1).

**Output (code/Task_04_numerical_errors.py):**
```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## C. Parameter change and effect
Changed approx_value from 1.414 to 1.4142 (code/Task_04_modified_parameter.py).

| approx_value | Absolute error | Relative error |
|---|---|---|
| 1.414 | 0.00021356 | 0.01510114% |
| 1.4142 | 0.00001356 | 0.00095900% |

(Explain in your words: error fell about 15.7 times because the approximation is closer to sqrt(2); the other lines are unchanged since they don't use approx_value.)

## D. Interpretation
(Explain in your words: why 0.1 + 0.2 != 0.3 in binary; why np.isclose is used; catastrophic cancellation in the direct formula for tiny x, where the exact limit is 0.5 and the direct form drifts to 0.50004445 at x = 1e-12 while the stable form stays correct.)

## E. Modified program: summing one million 0.10 KES sales
Code: code/Task_04_modified_money_sum.py

Assumptions: every sale is exactly 0.10 KES; the true total is 100,000.00 KES.

**Output:**
```
Method, Total, Abs error
float64 loop 100000.00000133 0.00000133
np.sum 100000.00000000 0.00000000
math.fsum 100000.00000000 0.00000000
float32 running 100958.34375000 958.34375000
integer cents 100000.00000000 0.00000000
Loop total == 100000.0 ? False
np.isclose(loop total, 100000.0) ? True
```

(Interpretation in your own words, as above.)