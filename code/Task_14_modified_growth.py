import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

years = np.array([0, 10, 20, 30, 40], dtype=float)
population = np.array([100, 134, 181, 243, 327], dtype=float)  # thousands

def exponential(t, P0, r):
    return P0 * np.exp(r * t)

(P0, r), cov = curve_fit(exponential, years, population, p0=[100, 0.03])
predicted = exponential(years, P0, r)
rmse = np.sqrt(np.mean((population - predicted)**2))

print(f"Fitted model: P = {P0:.2f} * exp({r:.5f} t)")
print(f"Growth rate: {100 * r:.3f} % per year")
print(f"Doubling time: {np.log(2) / r:.2f} years")
print(f"RMSE: {rmse:.3f} thousand")
print(f"Prediction at year 50: {exponential(50, P0, r):.1f} thousand")

t_plot = np.linspace(0, 50, 200)
plt.scatter(years, population, label="Data")
plt.plot(t_plot, exponential(t_plot, P0, r), label="Exponential fit")
plt.xlabel("Years since base year")
plt.ylabel("Population (thousands)")
plt.title("Exponential population growth")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/task14_growth.png", dpi=120)
plt.show()