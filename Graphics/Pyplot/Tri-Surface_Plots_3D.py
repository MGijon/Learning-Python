###
###     TRIANGULAR MESH
### ************************

##
## Example 1:
## ==========


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


n_radii = 8
n_angles = 36

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint = False)

# Repeat all angles for each radius.
angles = np.repeat(angles[..., np.newaxis], n_radii, axis = 1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z to make the pringle surface.
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.plot_trisurf(x, y, z, linewidth = 0.2, antialiased = True)

plt.title('Tri-Surface_Plots_3D_TRIANGULAR_MESH_example1')
plt.savefig('Tri-Surface_Plots_3D_TRIANGULAR_MESH_example1.png')
plt.show()


##
## Example 2 (a):
## ==============

'''
This one demonstrates use of plot_trisurf's triangles argument
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri


fig = plt.figure(figsize = plt.figaspect(0.5))

# Make a mesh in the space of parameterisation variables u and v
u = np.linspace(0, 2.0 * np.pi, endpoint = True, num = 50)
v = np.linspace(-0.5, 0.5, endpoint = True, num = 10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

# This is the Mobius mapping, taking a u, v pair and returning an x, y, z
# triple
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(u, v)

# Plot the surface.  The triangles in parameter space determine which x, y, z
# points are connected by an edge.
ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.plot_trisurf(x, y, z, triangles = tri.triangles, cmap = plt.cm.Spectral)
ax.set_zlim(-1, 1)


##
## Example 2 (b):
## ==============

'''
This one sets a Triangulation object's mask and passes the object directly
to plot_trisurf.
'''

# Make parameter spaces radii and angles.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint = False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis = 1)
angles[:, 1::2] += np.pi/n_angles

# Map radius, angle pairs to x, y, z points.
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(angles*3.0)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = mtri.Triangulation(x, y)

# Mask off unwanted triangles.
xmid = x[triang.triangles].mean(axis = 1)
ymid = y[triang.triangles].mean(axis = 1)
mask = np.where(xmid**2 + ymid**2 < min_radius**2, 1, 0)
triang.set_mask(mask)

# Plot the surface.
ax = fig.add_subplot(1, 2, 2, projection = '3d')
ax.plot_trisurf(triang, z, cmap = plt.cm.CMRmap)

plt.title('Tri-Surface_Plots_3D_TRIANGULAR_MESH_examples_2_(a)_(b)')
plt.savefig('Tri-Surface_Plots_3D_TRIANGULAR_MESH_examples_2_(a)_(b).png')
plt.show()



# source : https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html