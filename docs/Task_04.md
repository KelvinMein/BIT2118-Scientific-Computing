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

The absolute error fell from 0.00021356 to 0.00001356, about 15.7 times smaller, because 1.4142 is closer to the true value of the square root of 2 (1.41421356) than 1.414 is. The relative error shrank by the same factor, since it is the absolute error divided by the same number. The other lines of output did not change because they do not use approx_value.

## D. Interpretation
Computers store numbers in binary, and 0.1 and 0.2 cannot be written exactly in binary, just as 1/3 cannot be written exactly in decimal. Adding them gives 0.30000000000000004, so an exact == comparison returns False. np.isclose accepts a tiny tolerance, so it returns True. In the direct formula (sqrt(1+x) - 1)/x, a tiny x makes sqrt(1+x) almost equal to 1, so the subtraction cancels most of the correct digits and leaves mostly round-off noise. At x = 1e-12 the direct result was 0.50004445 instead of 0.5, while the stable form 1/(sqrt(1+x)+1) stayed correct because it has no subtraction of nearly equal numbers.
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

The float64 loop ended about 1.3e-6 KES from the true total of 100,000 because 0.10 cannot be stored exactly and each of the million additions adds a tiny error. np.sum and math.fsum were almost exact because they limit how errors build up. The float32 total was off by about 958 KES because it keeps only about 7 significant digits. For money, integer cents or Decimal are safer than floats, and results should be compared with a tolerance, not ==.