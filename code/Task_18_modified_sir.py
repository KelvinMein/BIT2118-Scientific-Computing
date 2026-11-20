import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N = 10_000
beta, gamma = 0.4, 0.1

def sir(t, y):
    S, I, R = y
    return [-beta * S * I / N,
            beta * S * I / N - gamma * I,
            gamma * I]

y0 = [N - 10, 10, 0]
t_eval = np.linspace(0, 120, 400)
sol = solve_ivp(sir, (0, 120), y0, t_eval=t_eval, rtol=1e-8, atol=1e-10)

S, I, R = sol.y
peak = np.argmax(I)

print("Solver success:", sol.success)
print(f"R0 = beta/gamma = {beta / gamma:.1f}")
print(f"Peak infections: {I[peak]:.0f} people on day {sol.t[peak]:.1f}")
print(f"Total ever infected by day 120: {R[-1] + I[-1]:.0f} ({100 * (R[-1] + I[-1]) / N:.1f} %)")
print(f"Population conserved: max |S+I+R-N| = {np.max(np.abs(S + I + R - N)):.2e}")

plt.plot(sol.t, S, label="Susceptible")
plt.plot(sol.t, I, label="Infected")
plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Days")
plt.ylabel("People")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/task18_sir.png", dpi=120)
plt.show()