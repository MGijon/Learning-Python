import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style = "white")

# Load the example planets dataset
planets = sns.load_dataset("planets")

# Make a range of years to show categories with no observations
years = np.arange(2000, 2015)

# Draw a count plot to show the number of planets discovered each year
g = sns.factorplot(x = "year", data = planets, kind = "count",
                   palette = "BuPu", size = 6, aspect = 1.5, order = years)
g.set_xticklabels(step=2)

# save and show the picture
plt.savefig('Barplot_timeseries.png')
plt.title('Barplot timeseries')
plt.show()

# source : https://seaborn.pydata.org/examples/timeseries_of_barplots.html