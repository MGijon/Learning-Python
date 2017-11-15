import numpy as np
from scipy import linalg

### ======
### BASICS
### ======


##
## Inverse Matriz
## ==============

a = np.array([[1., 2.], [3., 4.]])
print(a)
a_inv = linalg.inv(a)
print(a_inv)

# Chek the calculation

print(np.dot(a, a_inv))


##
## Solve Ax = b
## ============

b = np.array([45., 40.])
x = linalg.solve(a, b)

print(x)


##
## Determinant
## ===========

det_a = linalg.det(a)

print(det_a)


##
## Kronecker product
## =================

kron = linalg.kron(a, a_inv)
print(kron)

##
## Others
## ======

# (1): tril
# ---

# Make a copy of a matrix with elements above the k-th diagonal zeroed
# k == 0 is the main diagonal, k < 0 subdiagonal and k > 0 superdiagonal.
print(linalg.tril(kron))

print(linalg.tril(kron, k = -1))
print(linalg.tril(kron, k = 1))

# (2): triu
# ---

# Make a copy of a matrix with elements above the k-th diagonal zeroed
# k == 0 is the main diagonal, k < 0 subdiagonal and k > 0 superdiagonal.
print(linalg.triu(kron))

print(linalg.triu(kron, k = -1))
print(linalg.triu(kron, k = 1))

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################


### ======
### BASICS
### ======

###################################################################################################

# source : https://docs.scipy.org/doc/scipy/reference/linalg.html