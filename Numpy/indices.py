import numpy as np
'''
Return an array representing the indices of a grid.

Compute an array where the subarrays contain index values 0,1,... varying only along the corresponding axis.
'''

print("Example 1:")

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)

grid = np.indices((2, 3))
print(grid)                            # [[[0 0 0]
                                       #   [1 1 1]]

                                       #  [[0 1 2]
                                       #   [0 1 2]]]

print(grid.shape)                      # (2, 2, 3)

# row indices
print(grid[0])                         # [[0 0 0]
                                       #  [1 1 1]]
# column indices
print(grid[1])                         # [[0 1 2]
                                       #  [0 1 2]]

print(x[grid[0], grid[1]])             # [[ 1.  2.  3.]
                                       #  [ 6.  7.  8.]]

print("Example 2:")

x = np.arange(20).reshape(5, 4)

row, col = np.indices((2, 3))

print(x[row, col])                     # [[0 1 2]
                                       #  [4 5 6]]