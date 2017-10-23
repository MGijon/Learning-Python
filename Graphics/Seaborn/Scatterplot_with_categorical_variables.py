import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style = "whitegrid", palette = "muted")

# Load the example iris dataset
iris = sns.load_dataset("iris")

# "Melt" the dataset to "long-form" or "tidy" representation
iris = pd.melt(iris, "species", var_name = "measurement")

# Draw a categorical scatterplot to show each observation
sns.swarmplot(x = "measurement", y = "value", hue = "species", data = iris)

# save and show the picture
plt.savefig('Scatterplot_with_categorical_variables.png')
plt.title('Scatterplot with categorical variables')
plt.show()

# source : https://seaborn.pydata.org/examples/scatterplot_categorical.html