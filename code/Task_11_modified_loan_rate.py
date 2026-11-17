from scipy.optimize import root_scalar

principal = 100_000
payment = 9_200
months = 12

def f(r):
    return payment * (1 - (1 + r)**-months) / r - principal

def df(r):
    h = 1e-8
    return (f(r + h) - f(r - h)) / (2 * h)

newton = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.01, x1=0.03, method="secant", xtol=1e-12)

r = newton.root
print(f"Monthly rate (Newton): {r:.6%}")
print(f"Monthly rate (Secant): {secant.root:.6%}")
print(f"Newton iterations: {newton.iterations}, Secant iterations: {secant.iterations}")
print(f"Annual equivalent rate: {(1 + r)**12 - 1:.4%}")
print(f"Total repaid: {payment * months:,} KES, total interest: {payment * months - principal:,} KES")