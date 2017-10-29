import matplotlib.pyplot as plt
import numpy as np


##
## Example 1:
## =========

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.random(20)
y = np.random.random(20)


plt.figure()
plt.subplot(211)

plt.plot(x, y, 'r', lw = 3)
plt.scatter(x, y, s = 120)

plt.title('Lines on top of dots')

# Scatter plot on top of lines
plt.subplot(212)

plt.plot(x, y, 'r', zorder = 1, lw = 3)
plt.scatter(x, y, s = 120, zorder = 2)
plt.title('Dots on top of lines')

plt.savefig('Zorder_example_1.png')
plt.show()


##
## Example 2:
## =========

x = np.linspace(0, 2*np.pi, 100)

plt.figure()

plt.plot(x, np.sin(x), linewidth = 10, color = 'black', label = 'zorder = 10', zorder = 10)  # on top
plt.plot(x, np.cos(1.3*x), linewidth = 10, color = 'red', label = 'zorder = 1', zorder = 1)  # bottom
plt.plot(x, np.sin(2.1*x), linewidth = 10, color = 'green', label = 'zorder = 3', zorder = 3)

plt.axhline(0, linewidth = 10, color = 'blue', label = 'zorder=2', zorder = 2)

plt.title('Custom order of elements')

l = plt.legend()
l.set_zorder(20)  # put the legend on top

plt.savefig('Zorder_example_2.png')
plt.show()



# source : https://matplotlib.org/devdocs/gallery/misc/zorder_demo.html#sphx-glr-gallery-misc-zorder-demo-py