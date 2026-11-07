import math
import numpy as np

N = 1_000_000
price = 0.10
true_total = 100_000.00

loop_total = 0.0
for _ in range(N):
    loop_total += price

numpy_total = np.sum(np.full(N, price))
fsum_total = math.fsum([price] * N)
f32_total = np.cumsum(np.full(N, price, dtype=np.float32))[-1]
cents_total = (10 * N) / 100

results = {
    "float64 loop": loop_total,
    "np.sum": numpy_total,
    "math.fsum": fsum_total,
    "float32 running": float(f32_total),
    "integer cents": cents_total,
}

print("Method, Total, Abs error")
for name, value in results.items():
    print(name, format(value, ".8f"), format(abs(value - true_total), ".8f"))

print("Loop total == 100000.0 ?", loop_total == true_total)
print("np.isclose(loop total, 100000.0) ?", np.isclose(loop_total, true_total))
