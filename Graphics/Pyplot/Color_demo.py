import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots(facecolor = 'darkslategray')
ax.plot(t, s, 'C1')
ax.set_xlabel('time (s)', color = 'C1')
ax.set_ylabel('voltage (mV)', color = '0.5')  # grayscale color
ax.set_title('Title', color = '#afeeee')

plt.savefig('Color_demo_example_1.png')
plt.show()


# source : https://matplotlib.org/gallery/color/color_demo.html#sphx-glr-gallery-color-color-demo-py