from matplotlib import pyplot as plt
import numpy as np
import matplotlib

# Fixing random state for reproducibility
np.random.seed(19680801)


x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 + 500

plt.scatter(x, y, s, c = "g", alpha = 0.5, marker = r'$\clubsuit$', label = "Luck")
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc = 2)

plt.title('Scatter Symbol trebol')
plt.savefig('Scatter_Symbol_trebol.png')
plt.show()

# source : https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/scatter_symbol.html#sphx-glr-gallery-lines-bars-and-markers-scatter-symbol-py