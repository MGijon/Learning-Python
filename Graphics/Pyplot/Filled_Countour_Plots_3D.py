##
## Example 1:
## ==========

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection = '3d')
X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contourf(X, Y, Z, cmap = cm.coolwarm)
ax.clabel(cset, fontsize = 9, inline = 1)

plt.title('Filled Countour Plots 3D example 1')
plt.savefig('Filled_Countour_Plots_3D_example1.png')
plt.show()

##
## Example 2:
## ==========

fig = plt.figure()
ax = fig.gca(projection = '3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride = 8, cstride = 8, alpha = 0.3)
cset = ax.contourf(X, Y, Z, zdir = 'z', offset = -100, cmap = cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir = 'x', offset = -40, cmap = cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir = 'y', offset = 40, cmap = cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.title('Filled Countour Plots 3D example 2')
plt.savefig('Filled_Countour_Plots_3D_example2.png')
plt.show()


# source : https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html