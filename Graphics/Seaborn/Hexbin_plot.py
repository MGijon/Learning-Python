import numpy as np
from scipy.stats import kendalltau
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style = "ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size = 1000)
y = -.5 * x + rs.normal(size = 1000)

sns.jointplot(x, y, kind = "hex", stat_func = kendalltau, color = "#4CB391")

# save and show the picture
plt.savefig('Hexbin_plot.png')
plt.show()


# source : https://seaborn.pydata.org/examples/hexbin_marginals.html