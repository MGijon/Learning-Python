import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

df = sns.load_dataset("iris")

g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot, lw=3)

# save and show the picture
plt.savefig('Paired_Density_and_Scatterplot_Matrix.png')
plt.show()


# source : https://seaborn.pydata.org/examples/pair_grid_with_kde.html