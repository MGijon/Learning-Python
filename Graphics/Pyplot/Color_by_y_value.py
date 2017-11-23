import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

upper = 0.77
lower = -0.77


supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where(np.logical_or(s < lower, s > upper), s)

fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)

plt.savefig('Color_by_y_value_example_1.png')
plt.show()


# source : https://matplotlib.org/gallery/color/color_by_yvalue.html#sphx-glr-gallery-color-color-by-yvalue-py