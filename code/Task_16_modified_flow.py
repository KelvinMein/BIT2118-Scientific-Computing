import numpy as np
from scipy.integrate import simpson, quad

# Part 1: borehole pump flow rate (litres per minute) every 10 minutes
minutes = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)
flow_lpm = np.array([0.0, 30.0, 45.0, 50.0, 48.0, 40.0, 25.0])

volume_trap = np.trapezoid(flow_lpm, minutes)
volume_simp = simpson(flow_lpm, x=minutes)
print(f"Volume pumped (trapezoid): {volume_trap:.1f} litres")
print(f"Volume pumped (Simpson):   {volume_simp:.1f} litres")

# Part 2: accuracy test on f(x) = sin(x) from 0 to pi, exact integral = 2
print()
print(f"{'points':>8}{'trapezoid err':>16}{'Simpson err':>16}")
for n in (5, 9, 17, 33):
    x = np.linspace(0, np.pi, n)
    y = np.sin(x)
    print(f"{n:>8}{abs(np.trapezoid(y, x) - 2):>16.2e}{abs(simpson(y, x=x) - 2):>16.2e}")

value, error_estimate = quad(np.sin, 0, np.pi)
print(f"quad result: {value:.12f}, estimated error {error_estimate:.1e}")