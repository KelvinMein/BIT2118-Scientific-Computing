# Task 11: Root Finding: Newton-Raphson and Secant Methods

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: cash flows [-10000, 3000, 3500, 4000, 2500] (an outlay followed by four annual inflows), starting guesses 0.10 for Newton and 0.05 and 0.20 for Secant, tolerance 1e-12.
Operations: the internal rate of return (IRR) is the rate r where NPV(r) = sum of cash_t / (1 + r)^t is zero. Newton-Raphson repeats r_new = r - NPV(r)/NPV'(r) using the analytic derivative. Secant replaces the derivative with a slope estimated from the two latest points.

**Output (code/Task_11_newton_secant.py):**
```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method:  11.542461%
NPV at Newton solution:   0.000000
Newton iterations: 4
Secant iterations: 7
```

## C. Parameter change and effect
Changed the first inflow from 3000 to 2000 (code/Task_11_modified_parameter.py).

| | First inflow 3000 | First inflow 2000 |
|---|---|---|
| Total inflows | 12,000 | 11,000 |
| IRR (Newton) | 11.542461% | 7.418517% |
| IRR (Secant) | 11.542461% | 7.418517% |
| Newton iterations | 4 | 5 |
| Secant iterations | 7 | 6 |

Cutting the first-year inflow by 1,000 (about 8% of total inflows) lowered the IRR by about 4.1 percentage points, from 11.54% to 7.42%. The project is sensitive because it only just pays back (11,000 against 10,000), and the first-year cash is discounted the least, so it counts the most. Both methods still agree, and the iteration counts changed only slightly because they start close to the root.

## D. Interpretation
The IRR of 11.54% is the yearly return at which the present value of the inflows exactly equals the 10,000 invested. Check: at r = 0.1154 the discounted inflows are 2689.6 + 2813.2 + 2882.4 + 1615.1 = 10,000.3, so NPV is about 0 (printed as 0.000000). If the cost of capital is below 11.54% the project is worthwhile, and if it is above, it is not. Newton-Raphson needed 4 iterations and Secant 7. Newton uses the tangent line from the exact derivative and converges quadratically, roughly doubling the number of correct digits each step. Secant needs no derivative formula, which is useful when the derivative is hard to obtain, at the cost of a few more steps (superlinear convergence).

## E. Modified program: interest rate of a loan
Code: code/Task_11_modified_loan_rate.py

Assumptions: a loan of 100,000 KES received now and repaid in 12 equal month-end instalments of 9,200 KES; the monthly rate r solves 9200 x (1 - (1 + r)^-12) / r = 100000; the annual equivalent is (1 + r)^12 - 1. The derivative is approximated numerically with a central difference.

**Output:**
```
Monthly rate (Newton): 1.555981%
Monthly rate (Secant): 1.555981%
Newton iterations: 4, Secant iterations: 6
Annual equivalent rate: 20.3555%
Total repaid: 110,400 KES, total interest: 10,400 KES
```

The monthly rate is about 1.56%, which is an annual equivalent of 20.36%. The shop repays 110,400 KES, so the interest is 10,400 KES, which looks like a flat 10.4%. But the balance falls every month, so the borrower is using less than 100,000 KES for most of the year, and the true cost is much higher than 10.4%. This is why the rate has to be found by solving an equation and cannot be read off directly. Both methods agree, and substituting the rate back gives an annuity value of 100,000. Newton took 4 iterations and Secant 6, so both converge quickly from a rough starting guess.