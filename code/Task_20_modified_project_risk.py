import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
N = 100_000

design = rng.triangular(4, 6, 10, N)
build = rng.triangular(10, 14, 22, N)
test = rng.triangular(3, 5, 9, N)
total = design + build + test

deadline = 30.0
on_time = (total <= deadline).mean()

print(f"Most-likely total (sum of modes): {6 + 14 + 5} days")
print(f"Simulated mean duration: {total.mean():.2f} days")
print(f"Simulated standard deviation: {total.std():.2f} days")
print(f"Probability of finishing within {deadline:.0f} days: {on_time:.2%}")
print(f"90th percentile duration: {np.percentile(total, 90):.2f} days")

# Pi estimate as an accuracy check of the random generator
pts = rng.random((N, 2))
pi_est = 4 * np.mean(np.sum(pts**2, axis=1) <= 1)
print(f"Pi estimate from {N} points: {pi_est:.4f} (true 3.1416)")

plt.hist(total, bins=60)
plt.axvline(deadline, color="red", linestyle="--", label="Deadline")
plt.xlabel("Total project duration (days)")
plt.ylabel("Number of simulations")
plt.title("Monte Carlo project duration")
plt.legend()
plt.savefig("docs/images/task20_project.png", dpi=120)
plt.show()