import numpy as np
import matplotlib.pyplot as plt

r, K, P0 = 0.8, 1000.0, 50.0
end_time = 12.0

def exact(t):
    return K / (1 + (K - P0) / P0 * np.exp(-r * t))

def euler(h):
    t = np.arange(0, end_time + h / 2, h)
    P = np.zeros_like(t)
    P[0] = P0
    for i in range(len(t) - 1):
        P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
    return t, P

print(f"{'h (hours)':>10}{'Euler P(12)':>14}{'Exact P(12)':>14}{'Max error':>12}")
for h in (2.0, 1.0, 0.5, 0.1):
    t, P = euler(h)
    print(f"{h:>10}{P[-1]:>14.2f}{exact(end_time):>14.2f}{np.max(np.abs(P - exact(t))):>12.2f}")

t_fine = np.linspace(0, end_time, 300)
plt.plot(t_fine, exact(t_fine), label="Exact")
for h in (2.0, 0.5):
    t, P = euler(h)
    plt.plot(t, P, marker="o", markersize=3, label=f"Euler h={h}")
plt.xlabel("Time (hours)")
plt.ylabel("Population")
plt.title("Logistic growth: Euler vs exact")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/task17_logistic.png", dpi=120)
plt.show()