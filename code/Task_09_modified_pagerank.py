import numpy as np

pages = ["Home", "News", "Blog", "Shop", "About"]

# links[i][j] = 1 means page j links to page i
links = np.array([
    [0, 1, 1, 1, 1],   # Home receives links from News, Blog, Shop, About
    [1, 0, 0, 0, 0],   # News  receives a link from Home
    [1, 1, 0, 0, 0],   # Blog  receives links from Home and News
    [0, 0, 1, 0, 0],   # Shop  receives a link from Blog
    [0, 0, 0, 1, 0]    # About receives a link from Shop
], dtype=float)

# Column-stochastic matrix: each column sums to 1
M = links / links.sum(axis=0)

d = 0.85
n = len(pages)
G = d * M + (1 - d) / n * np.ones((n, n))

# Power iteration
rank = np.ones(n) / n
for k in range(1, 201):
    new_rank = G @ rank
    if np.linalg.norm(new_rank - rank, 1) < 1e-12:
        break
    rank = new_rank

# Compare with the eigenvector from np.linalg.eig
values, vectors = np.linalg.eig(G)
i = np.argmax(np.real(values))
eig_rank = np.abs(np.real(vectors[:, i]))
eig_rank = eig_rank / eig_rank.sum()

print("Power iteration steps:", k)
print("Dominant eigenvalue of G:", round(np.real(values[i]), 6))
print("PageRank scores (power iteration):")
for name, score in sorted(zip(pages, rank), key=lambda t: -t[1]):
    print(f"  {name}: {score:.4f}")
print("Matches eig result:", np.allclose(rank, eig_rank))