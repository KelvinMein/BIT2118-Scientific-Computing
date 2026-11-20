import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 2, 4, 6, 8, 10, 12, 14], dtype=float)
speed = np.array([0.0, 6.0, 12.5, 18.0, 20.0, 19.0, 12.0, 4.0])  # m/s

acceleration = np.gradient(speed, time)

for t, v, a in zip(time, speed, acceleration):
    print(f"t={t:4.0f} s, speed={v:5.1f} m/s, acceleration={a:6.2f} m/s^2")

i_max = np.argmax(acceleration)
i_min = np.argmin(acceleration)
print(f"Strongest acceleration: {acceleration[i_max]:.2f} m/s^2 at t = {time[i_max]:.0f} s")
print(f"Strongest braking: {acceleration[i_min]:.2f} m/s^2 at t = {time[i_min]:.0f} s")

plt.plot(time, acceleration, marker="o")
plt.axhline(0, linewidth=0.8)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration estimated from speed readings")
plt.grid(True)
plt.savefig("docs/images/task15_acceleration.png", dpi=120)
plt.show()