# Basic histogram, all parameters set by defaut

import matplotlib.pyplot as plt
import numpy as np

gaussian_numbers = np.random.randn(1000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()