# Modified: model degree changed (1, 2 and 3) to compare fits
import numpy as np

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

for degree in (1, 2, 3):
    coeffs = np.polyfit(users, response_ms, degree)
    predicted = np.polyval(coeffs, users)
    rmse = np.sqrt(np.mean((response_ms - predicted)**2))
    at_400 = np.polyval(coeffs, 400)
    print(f"Degree {degree}: RMSE = {rmse:.2f} ms, prediction at 400 users = {at_400:.2f} ms")