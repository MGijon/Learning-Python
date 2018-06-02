import numpy as np

'''
THE N-DIMENSIONAL ARRAY
=======================

PARAMETERS:
----------
    shape : tuple of ints                               "de fuera a dentro"
            Shape of created array.
    dtype : data-type, optional
            Any object that can be interpreted as a numpy data type.
    buffer : object exposing buffer interface, optional
            Used to fill the array with data.
    offset : int, optional
            Offset of array data in buffer.
    strides : tuple of ints, optional
            Strides of data in memory.
    order : {‘C’, ‘F’}, optional
            Row-major (C-style) or column-major (Fortran-style) order.

'''

##  CONSTRUCTOR:
##  ============

# if we do this just obtain a regular python list

y = [[1, 2], [3, 4]]

print(type(y))                      # <class 'list'>

# this way just create an ndarray of this shape

x = np.ndarray([2, 2])

print(x)                            # [[  1.49166815e-154  -1.73060036e-077]
                                    #  [  2.16920450e-314   2.78136406e-309]]
print(x.shape)                      # (2, 2)

print('=========================')

# (1) this is an useful way to construct a ndarray, calling the class constructior:
# ---------------------------------------------------------------------------------

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

print(x)                            # [[1 2 3]
                                    #  [4 5 6]]
print(type(x))                      # <class 'numpy.ndarray'>
print(x.dtype)                      # int32
print(x.shape)                      # (2, 3)

# another example
y = np.array([1, 2, 3, 4], np.float64)

print(type(y))                      # <class 'numpy.ndarray'>
print(y.dtype)                      # float64
print(y.shape)                      # (4, )

print('=========================')

# (2) Zeros array:
# ----------------

# numpy.zeros(shape, dtype = float, order = 'C')

x = np.zeros((4, ))

print(x)                            # [ 0.  0.  0.  0.]
print(type(x))                      # <class 'numpy.ndarray'>
print(x.dtype)                      # float64
print(x.shape)                      # (4,)

# another example
y = np.zeros((3, 2))

print(y)                            # [[ 0.  0.]
                                    #  [ 0.  0.]
                                    #  [ 0.  0.]]
print(type(y))                      # <class 'numpy.ndarray'>
print(y.dtype)                      # float64
print(y.shape)                      # (3, 2)

print('=========================')

# (3) Empty array:
# ----------------

# numpy.empty(shape, dtype = float, order = 'C')

x = np.empty((4, ))

print(x)                            # [ 1.  2.  3.  4.]
print(type(x))                      # <class 'numpy.ndarray'>
print(x.dtype)                      # float64
print(x.shape)                      # (4,)

# another example
y = np.zeros((3, 2))

print(y)                            # [[ 0.  0.]
                                    #  [ 0.  0.]
                                    #  [ 0.  0.]]
print(type(y))                      # <class 'numpy.ndarray'>
print(y.dtype)                      # float64
print(y.shape)                      # (3, 2)

print('=========================')

##  SOME ATTRIBUTES:
##  ================


# (1) T:
# ------

x = np.array([[1., 2.], [3., 4.], [5., 6.]])

print(x.shape)                      # (3, 2)
print(x)                            # [[ 1.  2.]
                                    #  [ 3.  4.]
                                    #  [ 5.  6.]]

x = x.T

print(x.shape)                      # (2, 3)
print(x)                            # [[ 1.  3.  5.]
                                    #  [ 2.  4.  6.]]

# another example
x = np.array([1., 2., 3., 4.])

print(x.shape)                      # (4,)
print(x)                            # [ 1.  2.  3.  4.]

x = x.T

print(x.shape)                      # (4,)
print(x)                            # [ 1.  2.  3.  4.]

# Obs: in this case, transpose has no effect

print('=========================')


# (2) RESHAPE:
# ------------

# create a ndarray (15, ) of consecutive numbers
a = np.arange(15)


print(a)                            # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(type(a))                      # <class 'numpy.ndarray'>
print(a.shape)                      # (15, )

# now we give it a different shape:
a = a.reshape(3, 5)
print(a)                            # [[ 0  1  2  3  4]
                                    #  [ 5  6  7  8  9]
                                    #  [10 11 12 13 14]]
print(a.shape)                      # (3, 5)


print('=========================')

##  ARRAY INDEXING:
##  ===============


# (1) Basic Slicing and Indexing:
# -------------------------------


## INDEXING:

print('Array Indexing:')

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

print(x.shape)                      # (2, 3)    "two rows and three columns"

print(x[1, 2])                      # 6          The element of x in the *second* row, *third* column, namely, 6.


print('=========================')


## SLICING:

x = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.], dtype = np.float64)

print('Array Slicing:')

# Example 0:

print(x[0:4])                       # [ 1.  2.  3.  4.]
print(x[0:6])                       # [ 1.  2.  3.  4.  5.  6.]

# Example 1:

# start:stop:step

print(x[1:10:3])                    # [ 2.  5.  8.]
print(x[2:10:2])                    # [ 3.  5.  7.  9.]

# Example 2:

print(x[-1:10])                     # [ 10.]
print(x[-2:10])                     # [  9.  10.]
print(x[-3:10])                     # [  8.   9.  10.]

print(x[1:-9])                      # []
print(x[1:-8])                      # [ 2.]
print(x[1:-7])                      # [ 2.  3.]
print(x[0:-7])                      # [ 1.  2.  3.]

print(x[3:])                        # [  4.   5.   6.   7.   8.   9.  10.]
print(x[:4])                        # [ 1.  2.  3.  4.]

print('=========================')

x = np.array([[[1],[2],[3]], [[4],[5],[6]]])

print(x.shape)                      # (2, 3, 1)
print(x)                            # [[[1]
                                    #   [2]
                                    #   [3]]

                                    #  [[4]
                                    #   [5]
                                    #   [6]]]

# Example 3:

print(x[1:2])                       #  [[4]
                                    #   [5]
                                    #   [6]]]

print(x[1:])                        # prints the same as before
print(x[1::])                       # prints the same as before
print(x[1:2:1])                     # prints the same as before

print(x[0:])                        # [[[1]
                                    #   [2]
                                    #   [3]]

                                    # [[4]
                                    #  [5]
                                    #  [6]]]


print(x[1:1:1])                     # []
print(x[4:4:2])                     # []

print(x[0:4:2])                     # [[[1]
                                    #   [2]
                                    #   [3]]]

print(x[1:4:2])                     # [[[4]
                                    #   [5]
                                    #   [6]]]

# Example 4:

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)

print(x.shape)                      # (2, 5)
print(x)                            # [[  1.   2.   3.   4.   5.]
                                    #  [  6.   7.   8.   9.  10.]]


print(x[0:4])                       # [[  1.   2.   3.   4.   5.]
                                    #  [  6.   7.   8.   9.  10.]]

print(x[4:8])                       # []
print(x[8:])                        # []

print(x[0, 1])                      # 2.0                      indexing
print(x[0:1])                       # [[ 1.  2.  3.  4.  5.]]

print(x[0:2])                       # [[  1.   2.   3.   4.   5.]
                                    #  [  6.   7.   8.   9.  10.]]

print(x[:,1])                       # [ 2.  7.]                   all the rows, second column
print(x[1,:])                       # [  6.   7.   8.   9.  10.]  second row, all the columns
print(x[0, 3:4])                    # [ 4.]                       first row, 3-(3-1) column
print(x[1, 0:3])                    # [ 6.  7.  8.]               second row, columns from 0 to 2





# (1.1) ELLIPSIS:
# ---------------

# Expand to the number of : objects needed to make a selection tuple of the same length as x.ndim.
# There may only be a single ellipsis present.

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)

print(x[...,0])                     # [ 1.  6.]


x = np.array([[1., 2., 3.], [4., 5., 6.] , [7., 8., 9.]], dtype = np.float64)

print(x[...,0])                     # [ 1.  4.  7.]
print(x[...,1])                     # [ 2.  5.  8.]
print(x[...,2])                     # [ 3.  6.  9.]



# (1.2) NEWAXIS:
# --------------

# Each newaxis object in the selection tuple serves to expand the dimensions of the resulting selection
# by one unit-length dimension.
# The added dimension is the position of the newaxis object in the selection tuple.

x = np.array([[1., 2., 3.], [4., 5., 6.] , [7., 8., 9.]], dtype = np.float64)

print(x.shape)                   # (3, 3)

print(x[:,np.newaxis,:].shape)   # (3, 1, 3))
print(x[:,np.newaxis,:])         # [[[ 1.  2.  3.]]

                                 #  [[ 4.  5.  6.]]

                                 #  [[ 7.  8.  9.]]]

x = np.array([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.]], dtype = np.float64)
print('WORKING HERE!!!!')

print(x.shape)                    # (2, 5)

print(x[:, np.newaxis].shape)     # (2, 1, 5)
print(x[:, np.newaxis])           # [[[  1.   2.   3.   4.   5.]]

                                  #  [[  6.   7.   8.   9.  10.]]]


# (1) Advanced Indexing:
# ----------------------






# source 1 : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.html
# source 2 : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.zeros.html#numpy.zeros
# source 3 : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.empty.html#numpy.empty
# source 4 : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T
# source 5 : https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html#printing-arrays
# source 6 : https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#arrays-indexing
# source 7 : http://scipy-cookbook.readthedocs.io/items/Indexing.html
