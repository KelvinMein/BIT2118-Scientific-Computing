import numpy as np
import matplotlib.pyplot as plt

n = 50
A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.ones(n)          # uniform heat source

def jacobi(A, b, tol=1e-6, max_iter=20000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        x_new = (b - R @ x) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k
        x = x_new
    return x, max_iter

def gauss_seidel(A, b, tol=1e-6, max_iter=20000):
    x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        if np.linalg.norm(x - old, ord=np.inf) < tol:
            return x, k
    return x, max_iter

x_j, k_j = jacobi(A, b)
x_gs, k_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi iterations:", k_j)
print("Gauss-Seidel iterations:", k_gs)
print("Jacobi max error:", np.max(np.abs(x_j - x_exact)))
print("Gauss-Seidel max error:", np.max(np.abs(x_gs - x_exact)))
print("Peak temperature (exact):", x_exact.max())

plt.plot(x_exact, label="Direct solution")
plt.plot(x_gs, "--", label="Gauss-Seidel")
plt.xlabel("Position along rod (grid point)")
plt.ylabel("Temperature")
plt.title("Rod with uniform heat source")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/task8_rod.png", dpi=120)
plt.show()