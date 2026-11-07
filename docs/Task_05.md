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

Changing the rotation angle from 45 to 90 degrees turned the square a quarter turn instead of an eighth, so the matrix changed from [[1.414, -1.061], [1.414, 1.061]] to about [[0, -1.5], [2, 0]]. The point (1,0) moved from (1.414, 1.414) to (0, 2). The determinant stayed at 3, because a rotation changes the orientation of a shape but not its area. Only the scale values 2.0 and 1.5 set the determinant. Tiny values such as 1.22e-16 are floating-point stand-ins for 0, since cos 90 degrees cannot be stored exactly in binary.

## D. Interpretation
The transformation matrix first stretches the square by 2 along x and 1.5 along y, then rotates it by 45 degrees. Each column shows where an axis direction ends up. The determinant is 2 x 1.5 = 3, because a rotation has determinant 1, so the area of the square grows from 1 to 3. The printed 3.000000000000001 is round-off. A determinant of 0 would mean the shape collapses onto a line or a point, and the matrix would not be invertible, so the original points could not be recovered.

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

One matrix moves every corner of the plot consistently. Each map unit becomes 25 m in both directions, so the determinant is 25 x 25 = 625, which is the factor by which area grows. The 4 x 2 plot of 8 map units becomes 5000 square metres (100 m by 50 m). The 30 degree rotation turns the plot to align with north but does not change its area, which is why the area ratio equals the determinant. GIS and graphics software use this idea to convert coordinates and check sizes.