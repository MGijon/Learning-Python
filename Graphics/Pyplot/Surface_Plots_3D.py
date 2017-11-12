from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

####
####    COLOR MAP
#### *****************

##
## Example 1:
## ==========

fig = plt.figure()
ax = fig.gca(projection = '3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink = 0.5, aspect = 5)

plt.title('COLOR MAP .- antialiased = False')
plt.savefig('Surface_Plots_3d_COLOR_MAPS_example1.png')
plt.show()


##
## Example 2:
## ==========

fig = plt.figure()
ax = fig.gca(projection = '3d')

surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = True)

plt.title('COLOR MAP .- antialiased = True')
plt.savefig('Surface_Plots_3d_COLOR_MAPS_example2.png')
plt.show()


####
####    SOLID COLOR
#### *******************


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

##
## Example 3:
## ==========


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z, color = 'b')

plt.title('SOLID COLOR')
plt.savefig('Surface_Plots_3d_SOLID_COLOR_example1.png')
plt.show()

####
####    CHECKBOARD PATTERN
#### **************************

##
## Example 4:
## ==========

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


fig = plt.figure()
ax = fig.gca(projection = '3d')

# Make data.
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Create an empty array of strings with the same shape as the meshgrid, and
# populate it with two colors in a checkerboard pattern.
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype = str)
for y in range(ylen):
    for x in range(xlen):
        colors[x, y] = colortuple[(x + y) % len(colortuple)]

# Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(X, Y, Z, facecolors = colors, linewidth = 0)

# Customize the z axis.
ax.set_zlim(-1, 1)
ax.w_zaxis.set_major_locator(LinearLocator(6))

plt.title('CHECKBOARD PATTERN')
plt.savefig('Surface_Plots_3d_CHECKBOARD_PATTERN_example1.png')
plt.show()



# source : https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html