import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(22)
sns.set(color_codes = True)


##
## Example 1
## =========

# generate data
x = np.linspace(0, 15, 31)
data = np.sin(x) + np.random.rand(10, 31) + np.random.randn(10, 1)

ax = sns.tsplot(data = data)

# save and show the picture
plt.savefig('tsplot_1.png')
plt.show()


##
## Example 2
## =========

# load data
gammas = sns.load_dataset("gammas")

ax = sns.tsplot(time = "timepoint", value = "BOLD signal", unit = "subject", condition = "ROI", data = gammas)

# save and show the picture
plt.savefig('tsplot_2.png')
plt.show()


##
## Example 3
## =========

ax = sns.tsplot(data = data, err_style = "ci_bars", color = "g")

# save and show the picture
plt.savefig('tsplot_3.png')
plt.show()


##
## Example 4
## =========

ax = sns.tsplot(data=data, err_style="ci_bars", interpolate=False)

# save and show the picture
plt.savefig('tsplot_4.png')
plt.show()


##
## Example 5
## =========

ax = sns.tsplot(data = data, ci = [68, 95], color = "m")

# save and show the picture
plt.savefig('tsplot_5.png')
plt.show()


##
## Example 6
## =========

ax = sns.tsplot(data = data, estimator = np.median)

# save and show the picture
plt.savefig('tsplot_6.png')
plt.show()


##
## Example 7
## =========

ax = sns.tsplot(data = data, err_style = "boot_traces", n_boot = 500)

# save and show the picture
plt.savefig('tsplot_7.png')
plt.show()


##
## Example 8
## =========

ax = sns.tsplot(data = data, err_style = "unit_traces")

# save and show the picture
plt.savefig('tsplot_8.png')
plt.show()



# source : https://seaborn.pydata.org/generated/seaborn.tsplot.html#seaborn.tsplot