# Task 2: NumPy Arrays and Numerical Computation

Author: Kelvin Mein

## B. Inputs and mathematical operations

**Input:** `temperatures_c`, a NumPy array of 24 hourly temperature readings in degrees Celsius (from 17.5 to 29.4).

**Operations:**
- Mean = (sum of all readings) / 24 = 554.9 / 24
- Minimum and maximum of the array
- Vectorized conversion F = 1.8C + 32, applied to all 24 values in one expression without a loop

**Output (code/Task_02_numpy_arrays.py):**
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## C. Parameter change and effect

I changed the peak reading from 29.4 to 35.0 (a simulated heat spike). Code: `code/Task_02_modified_parameter.py`.

| | Original | Modified |
|---|---|---|
| Mean | 23.12 C | 23.35 C |
| Min | 17.50 C | 17.50 C |
| Max | 29.40 C | 35.00 C |

The peak rose by 5.6 C but the mean rose by only about 0.23 C (5.6 / 24), because one value is shared among 24 readings. The maximum changed fully since it is decided by that single reading. The minimum was unchanged. The first six Fahrenheit values are identical because the changed reading is the 13th, outside the printed slice. So a single extreme value moves the mean slightly but controls the maximum completely.

## D. Interpretation of output

- The mean (23.12 C) is the typical temperature across the day.
- The minimum (17.5 C) is the coldest hour, early morning before sunrise.
- The maximum (29.4 C) is the hottest hour, around midday.
- The range of about 11.9 C is the daily temperature swing.
- The Fahrenheit array holds the same information in another unit. The conversion is linear, so the shape of the data stays the same and only the scale changes.

## E. Modified program: vaccine cold-chain monitoring

Code: `code/Task_02_modified_cold_chain.py`

**Real-world case:** A clinic fridge stores vaccines that must stay between 2 C and 8 C. An IoT sensor logs the temperature every hour. The program finds the daily statistics, the hours outside the safe range, and converts readings to Kelvin.

**Assumptions:**
- Readings are exactly hourly and the sensor is accurate.
- The safe range is 2 C to 8 C.
- The door is opened more often in the middle of the day, which explains the rise.

**Input data:** 24 hourly fridge temperatures from 3.8 C to 8.8 C (see the code file).

**Output:**
```
Mean: 5.82 C, Min: 3.80 C, Max: 8.80 C
Hours out of safe range: 4
Hours (24h clock): [11 12 13 14]
First three Kelvin values: [277.35 277.15 277.05]
```

**Interpretation:** The mean of 5.82 C is inside the safe range, but it hides a problem. For 4 hours around midday the fridge exceeded 8 C, so the vaccines may have been compromised. A summary statistic alone is not enough, which is why a boolean mask `(x < min) | (x > max)` is useful for flagging the exact hours that break the rule.

**Note on rounding:** The exact mean is 139.8 / 24 = 5.825, but Python prints 5.82 because 5.825 cannot be stored exactly in binary floating point.