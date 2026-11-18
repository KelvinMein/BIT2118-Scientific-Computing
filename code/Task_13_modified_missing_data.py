import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([6, 8, 10, 14, 16, 18], dtype=float)
moisture = np.array([42.0, 40.0, 36.5, 28.0, 25.5, 24.0])

linear = interp1d(hours, moisture, kind="linear")
cubic = CubicSpline(hours, moisture)

for t in (12, 15):
    print(f"Hour {t}: linear = {float(linear(t)):.2f} %, cubic = {float(cubic(t)):.2f} %")

# Out-of-range check: extrapolation at hour 20 using the cubic spline
print(f"Cubic extrapolation at hour 20: {float(cubic(20)):.2f} % (not reliable)")

t_fine = np.linspace(6, 18, 200)
plt.scatter(hours, moisture, label="Measured")
plt.plot(t_fine, linear(t_fine), label="Linear")
plt.plot(t_fine, cubic(t_fine), label="Cubic spline")
plt.axvline(12, linestyle=":", color="gray")
plt.xlabel("Hour of day")
plt.ylabel("Soil moisture (%)")
plt.title("Estimating a missing sensor reading")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/task13_missing.png", dpi=120)
plt.show()