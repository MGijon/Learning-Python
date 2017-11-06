#Quiver_and_quiverkey

import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)


##
## Example 1:
## =========

plt.figure()
plt.title('Arrows scale with plot width, not view')

Q = plt.quiver(X, Y, U, V, units = 'width')
qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos = 'E', coordinates = 'figure')

plt.savefig('Quiver_and_quiverkey_example_1.png')
plt.show()


##
## Example 2:
## =========

plt.figure()
plt.title("pivot = 'mid'; every third arrow; units = 'inches'")

Q = plt.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], pivot = 'mid', units = 'inches')
qk = plt.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos = 'E', coordinates = 'figure')

# adding a scatter plot
plt.scatter(X[::3, ::3], Y[::3, ::3], color = 'r', s = 5)

plt.savefig('Quiver_and_quiverkey_example_2.png')
plt.show()


##
## Example 3:
## =========

plt.figure()
plt.title("pivot = 'tip'; scales with x view")

M = np.hypot(U, V)
Q = plt.quiver(X, Y, U, V, M, units = 'x', pivot = 'tip', width = 0.022, scale = 1 / 0.15)
qk = plt.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos = 'E', coordinates = 'figure')

# adding a scatter plot
plt.scatter(X, Y, color = 'k', s = 5)

plt.savefig('Quiver_and_quiverkey_example_3.png')
plt.show()


# source : https://matplotlib.org/devdocs/gallery/images_contours_and_fields/quiver_demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-demo-py