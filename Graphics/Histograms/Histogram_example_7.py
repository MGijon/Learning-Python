import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111) # == plt.figure()

x = np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed = 1, facecolor = 'b', alpha = 0.75)

plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Normal Distribution')
plt.axis([-3, 3, 0, .8])
plt.grid(True)

plt.annotate('max', xy = (0, 0.45), xytext = (0.3, 0.55),
             arrowprops = dict(facecolor = 'black', shrink = 0.05), )

plt.savefig('Histogram_example_7.png')

# OBS : arguments of xy and xytext are tuples

plt.show()