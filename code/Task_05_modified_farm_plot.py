import numpy as np

# Plot corners in map units: each row is [x, y]
corners = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 2.0],
    [0.0, 2.0]
])

# 1 map unit = 25 metres
scale = np.array([
    [25.0, 0.0],
    [0.0, 25.0]
])

# Rotate by 30 degrees to align with true north
angle = np.deg2rad(30)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

transformation = rotation @ scale
corners_m = corners @ transformation.T

# Area of the plot before and after, using the shoelace formula
def polygon_area(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

area_map = polygon_area(corners)
area_m = polygon_area(corners_m)

print("Corners in metres after rotation and scaling:\n", np.round(corners_m, 2))
print("Determinant of transformation:", round(np.linalg.det(transformation), 2))
print("Area in map units:", area_map)
print(f"Area in square metres: {area_m:.2f}")
print("Area ratio equals determinant:", np.isclose(area_m / area_map, np.linalg.det(transformation)))