# Task 3: Mathematical Functions and Vectorization

Author: Kelvin Mein

## B. Inputs and mathematical operations
**Input:** 1,000,000 simulated latency readings in milliseconds (uniform between 5 and 250, seed 42).

**Operations:** seconds = ms / 1000, then squared = seconds², computed two ways: a Python loop and a vectorized NumPy expression. `timeit` measures the time of each.

**Output (code/Task_03_vectorization.py):**
```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.3755 s
Vectorized time: 0.0224 s
Approximate speed-up: 16.8x
```

## C. Parameter change and effect
I reduced the number of readings from 1,000,000 to 10,000 (code/Task_03_modified_parameter.py).

| N readings | Loop time | Vectorized time | Speed-up |
|---|---|---|---|
| 1,000,000 | 0.3755 s | 0.0224 s | 16.8x |
| 10,000 | 0.0036 s | under 0.00005 s (printed as 0.0000) | about 93x (noisy) |

The loop time fell roughly 100 times when N fell 100 times, so the cost per element is about constant. The first five values are unchanged because seed 42 generates the same first numbers whatever the length. Speed-up varies between runs (16.8x and 31.1x on the same 1,000,000 readings), so it should be quoted as a range. At N = 10,000 the vectorized time is so small that the ratio is unreliable.

## D. Interpretation
Each output value is a latency in seconds squared, such as the squared-error term used in error calculations. The values are small because latencies are fractions of a second. Vectorization is faster because the loop runs interpreted Python once per element, while NumPy runs one compiled loop in C. The advantage matters for large datasets.

## E. Modified program: mobile-money tiered fees
Code: `code/Task_03_modified_mobile_fees.py`

**Case:** A mobile-money platform must compute the fee for 500,000 transactions with tiered rates and total the revenue.

**Assumptions (illustrative, not a real provider's tariff):**
- Amount up to 100 KES: fee 0
- 101 to 1,000 KES: fee 10
- 1,001 to 10,000 KES: fee 30
- Above 10,000 KES: 0.5% of the amount
- Amounts are uniform between 10 and 70,000 KES (seed 1)

**Output:**
```
Results identical: True
Total fee revenue: 87,687,840.01 KES
Average fee: 175.38 KES
Share of transactions with zero fee: 0.13%
Loop time: 0.3213 s
Vectorized time: 0.0125 s
Approximate speed-up: 25.8x
```

**Interpretation:** The loop and `np.select` results are identical, so vectorization changes only the speed. About 86% of transactions fall in the top tier, so the percentage fee drives the revenue. Only 0.13% pay no fee. The vectorized version was about 26 times faster, which matters when processing millions of transactions.