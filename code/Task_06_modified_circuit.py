import numpy as np

# Mesh-current equations (Kirchhoff's voltage law), units: ohms and volts
A = np.array([
    [10.0, -2.0, -3.0],
    [-2.0,  8.0, -1.0],
    [-3.0, -1.0,  9.0]
])

b = np.array([12.0, 0.0, -6.0])

currents = np.linalg.solve(A, b)
residual = b - A @ currents

print("Determinant of A:", round(np.linalg.det(A), 2))
print("Condition number:", round(np.linalg.cond(A), 2))
for i, current in enumerate(currents, start=1):
    print(f"I{i} = {current:.4f} A")
print("Verification A @ I:", A @ currents)
print("Residual norm:", np.linalg.norm(residual))