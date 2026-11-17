# Task 9: Eigenvalues and Eigenvectors

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: 4x4 adjacency matrix of a small network (links A-B, A-C, B-C, B-D, C-D).
Operations: np.linalg.eig, choosing the dominant eigenvalue and its eigenvector, normalising to scores that sum to 1, and verifying Av = lambda v.

**Output (code/Task_09_eigenvalues.py):**
```
Dominant eigenvalue: 2.5615528128088276
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 2.6921477609369894e-15
```

## C. Parameter change and effect
Added a link between A and D (code/Task_09_modified_parameter.py), so every node is connected to every other node.

**Output:**
```
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 0.0
```

| | Original | Modified |
|---|---|---|
| Dominant eigenvalue | 2.5616 | 3.0 |
| Scores of A and D | 0.2192 | 0.2500 |
| Scores of B and C | 0.2808 | 0.2500 |

Adding the single link A-D gave every node exactly 3 links, so the network became perfectly symmetric. The dominant eigenvalue rose from 2.56 to 3, which equals the number of links per node, and the four scores became equal. A and D gained importance, and B and C lost the advantage they had when they were the only nodes with 3 links.

## D. Interpretation
An eigenvector keeps its direction when the matrix is applied, and the eigenvalue says how much it is stretched (Av = lambda v). For an adjacency matrix, the dominant eigenvector gives each node an importance score that depends not only on how many links it has but also on how important its neighbours are. In the original network B and C have 3 links each and A and D have 2, so B and C score higher (0.2808 against 0.2192). By symmetry A and D get equal scores, and so do B and C. By hand, with eigenvector (a, b, b, a), the equations lambda a = 2b and lambda b = 2a + b give lambda squared minus lambda minus 4 = 0, so lambda = (1 + sqrt(17))/2 = 2.5616, which matches the program. The verification error of about 3e-15 is only round-off, so Av = lambda v holds.

## E. Modified program: PageRank of five web pages
Code: code/Task_09_modified_pagerank.py

Assumptions: five pages (Home, News, Blog, Shop, About); a link from page j to page i is an entry in column j; each page splits its importance equally among the pages it links to; damping factor 0.85; scores start equal at 0.2 each.

**Output:**
```
Power iteration steps: 35
Dominant eigenvalue of G: 1.0
PageRank scores (power iteration):
  Home: 0.3456
  Blog: 0.2521
  News: 0.1769
  Shop: 0.1371
  About: 0.0883
Matches eig result: True
```

The PageRank vector is the dominant eigenvector of the damped link matrix G, and its eigenvalue is 1, so the scores do not change when G is applied again. Home ranks first with 0.3456 because all four other pages link to it. Blog is second because it receives links from Home and News, and a link from a highly ranked page counts for more. About ranks last because only Shop links to it, and Shop itself has a low rank. Power iteration reached the same scores as np.linalg.eig in 35 steps by repeated multiplication, which is how the method scales to billions of pages where a full eigen-decomposition is impossible. The damping factor of 0.85 models a surfer who sometimes jumps to a random page, which keeps the scores well defined.