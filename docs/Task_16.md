# Task 16: Numerical Integration

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: smart-meter power readings (kW) every 2 hours from hour 0 to 12.
Operations: energy is the integral of power over time. The trapezoidal rule (np.trapezoid) joins points with straight lines and adds the areas of the trapezoids. Simpson's rule (scipy.integrate.simpson) fits parabolas through groups of three points.

**Output (code/Task_16_numerical_integration.py):**
```
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule:   15.800 kWh
Difference between estimates:  0.100 kWh
```

By hand, the trapezoids are 1.8 + 2.4 + 3.2 + 3.4 + 2.8 + 2.1 = 15.7 kWh.

## C. Parameter change and effect
Changed the peak reading at hour 6 from 1.8 kW to 3.0 kW (code/Task_16_modified_parameter.py).

| | Peak 1.8 kW | Peak 3.0 kW |
|---|---|---|
| Trapezoid | 15.700 kWh | 18.100 kWh |
| Simpson | 15.800 kWh | 19.000 kWh |
| Difference | 0.100 kWh | 0.900 kWh |

The trapezoid total rose by 2.4 kWh, which is the 1.2 kW increase times 2 hours (the peak touches two intervals, each giving it half weight). Simpson rose by 3.2 kWh, because it gives the middle point of each group of three a weight of 4 and the peak is such a middle point. When the data are smooth the two rules agree closely, but a sharp peak makes them disagree. The gap growing from 0.1 to 0.9 kWh is a warning that readings every 2 hours may be too coarse to capture the peak.

## D. Interpretation
The integral of power over time is the energy used, so the household used about 15.7 to 15.8 kWh over the 12 hours. The load rises to a peak of 1.8 kW at hour 6 and then falls. Both rules agree within 0.6% on this smooth curve. Simpson gives slightly more because the curve is concave near the peak, so straight segments cut the corner and underestimate. Without the true curve we cannot say which estimate is correct, only that they are close.

## E. Modified program: borehole pump volume and accuracy test
Code: code/Task_16_modified_flow.py

Assumptions: a pump flow rate in litres per minute is logged every 10 minutes for an hour, and the volume pumped is the integral of the flow rate. The accuracy of the rules is tested on sin(x) from 0 to pi, whose exact integral is 2.

**Output:**
```
Volume pumped (trapezoid): 2255.0 litres
Volume pumped (Simpson):   2303.3 litres

  points   trapezoid err     Simpson err
       5        1.04e-01        4.56e-03
       9        2.58e-02        2.69e-04
      17        6.43e-03        1.66e-05
      33        1.61e-03        1.03e-06
quad result: 2.000000000000, estimated error 2.2e-14
```

By hand, the trapezoid volume is 10 x (0/2 + 30 + 45 + 50 + 48 + 40 + 25/2) = 2255 litres. Simpson gives 2303.3 litres, about 2% more, because the flow curve is concave and straight segments underestimate it. In the accuracy test, each doubling of the intervals cuts the trapezoid error about fourfold (second order) and the Simpson error about sixteenfold (fourth order). At 33 points Simpson is about 1,500 times more accurate. The adaptive routine quad returns 2.000000000000 with an estimated error of 2.2e-14, because it chooses its own sample points until the error is tiny. For measured data at fixed times, Simpson is usually a better choice than the trapezoid rule if the data are smooth, while quad needs a function it can evaluate anywhere.