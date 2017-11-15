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

# Make a copy of a matrix with elements above the k-th diagonal zeroed.
# k == 0 is the main diagonal, k < 0 subdiagonal and k > 0 superdiagonal.
print(linalg.tril(kron))

print(linalg.tril(kron, k = -1))
print(linalg.tril(kron, k = 1))

# (2): triu
# ---

# Make a copy of a matrix with elements above the k-th diagonal zeroed.
# k == 0 is the main diagonal, k < 0 subdiagonal and k > 0 superdiagonal.
print(linalg.triu(kron))

print(linalg.triu(kron, k = -1))
print(linalg.triu(kron, k = 1))

###################################################################################################


### ===================
### EIGENVALUE PROBLEMS
### ===================

# (1): eig
# ---

# Solve an ordinary or generalized eigenvalue problem of a square matrix.

print(linalg.eig(a))

# (2): eigvals
# ---

# Compute eigenvalues from an ordinary or generalized eigenvalue problem.

print(linalg.eigvals(a))

###################################################################################################


### ===============
### DESCOMPOSITIONS
### ===============

# (1.a): lu
# ---

# Compute pivoted LU decomposition of a matrix.

P, L, U = linalg.lu(a)

print(P)
print(L)
print(U)

# (1.b): lu_factor

# Compute pivoted LU decomposition of a matrix.

lu, piv = linalg.lu_factor(a)

print(lu)                   # Matrix containing U in its upper triangle, and L in its lower triangle.
                            # The unit diagonal elements of L are not stored.
print(piv)                  # Pivot indices representing the permutation matrix P: row i of matrix was
                            # interchanged with row piv[i].

###################################################################################################


### ================
### MATRIX FUNCTIONS
### ================

###################################################################################################


### =======================
### MATRIX EQUATION SOLVERS
### =======================

###################################################################################################


### ===============================
### SKETCHES AND RANDOM PROJECTIONS
### ===============================

###################################################################################################


### ================
### SPECIAL MATRICES
### ================

###################################################################################################


### ==================
### LOW-LEVEL ROUTINES
### ==================

###################################################################################################


# source : https://docs.scipy.org/doc/scipy/reference/linalg.html