##
## Example 1:
## ==========

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np


# set up a figure twice as wide as it is tall
fig = plt.figure(figsize = plt.figaspect(0.5))

##  First subplot

# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection = '3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm,
                       linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink = 0.5, aspect = 10)


## Second subplot

# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection = '3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride = 10, cstride = 10)

plt.title('Subploting 3D example 1')
plt.savefig('Subploting_3D_example1.png')
plt.show()


##
## Example 2:
## ==========

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def f(t):
    s1 = np.cos(2*np.pi*t)
    e1 = np.exp(-t)
    return np.multiply(s1, e1)

## First subplot

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 2.0, 0.01)

# Twice as tall as it is wide.
fig = plt.figure(figsize = plt.figaspect(2.))
fig.suptitle('A tale of 2 subplots')
ax = fig.add_subplot(2, 1, 1)
l = ax.plot(t1, f(t1), 'bo',
            t2, f(t2), 'k--', markerfacecolor = 'green')
ax.grid(True)
ax.set_ylabel('Damped oscillation')

## Second subplot

ax = fig.add_subplot(2, 1, 2, projection = '3d')
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1,
                       linewidth = 0, antialiased = False)

ax.set_zlim3d(-1, 1)

plt.title('Subploting 3D example 2')
plt.savefig('Subploting_3D_example2.png')
plt.show()


# source : https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html