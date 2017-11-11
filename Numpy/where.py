import numpy as np

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)

print(np.where(x == 1))                         # (array([0]), array([0]))
print(np.where(x == [1., 2., 3., 4., 5.]))      # (array([0, 0, 0, 0, 0]), array([0, 1, 2, 3, 4]))
print(np.where(x > 5))                          # (array([1, 1, 1, 1, 1]), array([0, 1, 2, 3, 4]))