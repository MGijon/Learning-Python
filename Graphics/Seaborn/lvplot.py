import seaborn as sns
import matplotlib.pyplot as plt

# load data
tips = sns.load_dataset("tips")

# common style
sns.set_style("whitegrid")

##
## Example 1
## =========

ax = sns.lvplot(x = tips["total_bill"])

# save and show the picture
plt.savefig('lvplot_1.png')
plt.show()


##
## Example 2
## =========

ax = sns.lvplot(x = "day", y = "total_bill", data = tips)

# save and show the picture
plt.savefig('lvplot_2.png')
plt.show()


##
## Example 3
## =========

ax = sns.lvplot(x = "day", y = "total_bill", hue = "smoker", data = tips, palette = "Set3")

# save and show the picture
plt.savefig('lvplot_3.png')
plt.show()


##
## Example 4
## =========

ax = sns.lvplot(x = "day", y = "total_bill", hue = "time", data = tips, linewidth = 2.5)

# save and show the picture
plt.savefig('lvplot_4.png')
plt.show()


##
## Example 5
## =========

ax = sns.lvplot(x = "time", y = "tip", data = tips, order = ["Dinner", "Lunch"])

# save and show the picture
plt.savefig('lvplot_5.png')
plt.show()


##
## Example 6
## =========

# load new data
iris = sns.load_dataset("iris")
ax = sns.lvplot(data = iris, orient = "h", palette = "Set2")

# save and show the picture
plt.savefig('lvplot_6.png')
plt.show()


##
## Example 7
## =========

ax = sns.lvplot(x = "day", y = "total_bill", data = tips)
ax = sns.stripplot(x="day", y="total_bill", data = tips, size = 4, jitter = True, color = "gray")

# save and show the picture
plt.savefig('lvplot_7.png')
plt.show()


##
## Example 8
## =========

g = sns.factorplot(x = "sex", y = "total_bill", hue = "smoker", col = "time", data = tips, kind = "lv", size = 4, aspect = .7)

# save and show the picture
plt.savefig('lvplot_8.png')
plt.show()







# source : https://seaborn.pydata.org/generated/seaborn.lvplot.html#seaborn.lvplot