# Task 5: Matrix Algebra and Matrix Operations

Author: Kelvin Mein

## B. Inputs and mathematical operations
Inputs: four corners of a unit square, a 45 degree rotation matrix, and a scale matrix [[2, 0], [0, 1.5]].
Operations: matrix product rotation @ scale, transforming points with points @ T.T, and the determinant.

**Output (code/Task_05_matrix_algebra.py):**
```
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 3.000000000000001
```

## C. Parameter change and effect
Changed the rotation angle from 45 to 90 degrees (code/Task_05_modified_parameter.py).

| | Original (45°) | Modified (90°) |
|---|---|---|
| Matrix | [[1.414, -1.061], [1.414, 1.061]] | [[0, -1.5], [2, 0]] |
| Point (1,0) goes to | (1.414, 1.414) | (0, 2) |
| Point (1,1) goes to | (0.354, 2.475) | (-1.5, 2) |
| Determinant | 3.000000000000001 | 2.9999999999999996 |

(Explain in your words: the angle changes orientation, not size, so the determinant stays 3. Values like 1.22e-16 are floating-point stand-ins for 0.)

## D. Interpretation
(Explain in your words: what the matrix does to the square, why the determinant is 2 x 1.5 = 3, and what det = 0 would mean: the shape collapses and the matrix is not invertible.)

## E. Modified program: farm plot map conversion
Code: code/Task_05_modified_farm_plot.py

Assumptions: plot corners (0,0), (4,0), (4,2), (0,2) in map units; 1 map unit = 25 m; rotation of 30 degrees to align with north.

**Output:**
```
Corners in metres after rotation and scaling:
 [[  0.    0. ]
 [ 86.6  50. ]
 [ 61.6  93.3]
 [-25.   43.3]]
Determinant of transformation: 625.0
Area in map units: 8.0
Area in square metres: 5000.00
Area ratio equals determinant: True
```

(Interpretation in your own words.)