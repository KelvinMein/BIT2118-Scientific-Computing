import numpy as np

# 24 hourly fridge temperatures (deg C)
fridge_c = np.array([
    4.2, 4.0, 3.9, 3.8, 4.1, 4.5, 5.0, 5.8, 6.5, 7.2, 7.9, 8.4,
    8.8, 8.6, 8.1, 7.5, 6.9, 6.2, 5.6, 5.1, 4.8, 4.5, 4.3, 4.1
])

SAFE_MIN, SAFE_MAX = 2.0, 8.0

mean_t = np.mean(fridge_c)
min_t = np.min(fridge_c)
max_t = np.max(fridge_c)

# Boolean mask: True where reading is outside the safe range
unsafe = (fridge_c < SAFE_MIN) | (fridge_c > SAFE_MAX)
unsafe_hours = np.where(unsafe)[0]

# Vectorized conversion to Kelvin
fridge_k = fridge_c + 273.15

print(f"Mean: {mean_t:.2f} C, Min: {min_t:.2f} C, Max: {max_t:.2f} C")
print(f"Hours out of safe range: {unsafe.sum()}")
print("Hours (24h clock):", unsafe_hours)
print("First three Kelvin values:", fridge_k[:3])