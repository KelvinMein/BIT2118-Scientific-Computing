import numpy as np
import timeit

# Simulated transaction amounts in KES
rng = np.random.default_rng(1)
amounts = rng.uniform(10, 70_000, 500_000)

def fee_loop():
    fees = []
    for a in amounts:
        if a <= 100:
            fees.append(0.0)
        elif a <= 1000:
            fees.append(10.0)
        elif a <= 10000:
            fees.append(30.0)
        else:
            fees.append(0.005 * a)
    return np.array(fees)

def fee_vectorized():
    return np.select(
        [amounts <= 100, amounts <= 1000, amounts <= 10000],
        [0.0, 10.0, 30.0],
        default=0.005 * amounts
    )

loop_time = timeit.timeit(fee_loop, number=1)
vector_time = timeit.timeit(fee_vectorized, number=3) / 3

fees_loop = fee_loop()
fees_vec = fee_vectorized()

print("Results identical:", np.allclose(fees_loop, fees_vec))
print(f"Total fee revenue: {fees_vec.sum():,.2f} KES")
print(f"Average fee: {fees_vec.mean():.2f} KES")
print(f"Share of transactions with zero fee: {(fees_vec == 0).mean():.2%}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")