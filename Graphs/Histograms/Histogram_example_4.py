import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
bins = [0, 40, 60, 75, 90, 110, 125, 140, 160, 200]
hist, bins = np.histogram(x, bins = bins)

width = np.diff(bins)
center = (bins[:-1] + bins[1:]) / 2

fig, ax = plt.subplots(figsize=(8,3))
ax.bar(center, hist, align='center', width=width)
ax.set_xticks(bins)
#fig.savefig("Histogram_example_4.png")   # save the figure in a png file

plt.show()

plt.hist(x, bins = 50)
plt.savefig('Histogram_example_4_fill.png')

plt.show()