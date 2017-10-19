import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

bins, edges = np.histogram(x, 50, normed=1)
left,right = edges[:-1],edges[1:]

X = np.array([left,right]).T.flatten()
Y = np.array([bins,bins]).T.flatten()

'''
numpy.ndarray.T : Same as self.transpose(), except that self is returned if self.ndim < 2.
numpy.ndarray.flatten : Return a copy of the array collapsed into one dimension.
'''

plt.plot(X,Y)
plt.savefig('Histogram_example_5.png')

plt.show()

