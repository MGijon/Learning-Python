import numpy as np

'''
Return elements, either from x or y, depending on condition.

If only condition is given, return condition.nonzero().
'''

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)

print(np.where(x == 1))                         # (array([0]), array([0]))
print(np.where(x == [1., 2., 3., 4., 5.]))      # (array([0, 0, 0, 0, 0]), array([0, 1, 2, 3, 4]))
print(np.where(x > 5))                          # (array([1, 1, 1, 1, 1]), array([0, 1, 2, 3, 4]))

x = np.arange(9.).reshape(3, 3)
print(x)                                        # [[ 0.  1.  2.]
                                                #  [ 3.  4.  5.]
                                                #  [ 6.  7.  8.]]
print(np.where(x > 5))                          # (array([2, 2, 2]), array([0, 1, 2]))
print(x[np.where( x > 3.0 )])                   # [ 4.  5.  6.  7.  8.]
print(np.where(x < 5, x, -1))                   # [[ 0.  1.  2.]
                                                #  [ 3.  4. -1.]
                                                #  [-1. -1. -1.]]


'''
Now find the elements of x that are in a certain list:
'''

values = [3, 5, 6]
indexes = np.isin(x, values)
print(indexes)                                   # [[False False False]
                                                 #  [ True False  True]
                                                 #  [ True False False]]
print(np.where(indexes))                         # (array([1, 1, 2]), array([0, 2, 0]))
print(x[np.where(indexes)])                      # [ 3.  5.  6.]


# source : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.where.html