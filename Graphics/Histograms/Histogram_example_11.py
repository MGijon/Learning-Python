import matplotlib.pyplot as plt
import numpy as np


# Three subplots sharing both x/y axes
f, (ax1, ax2, ax3) = plt.subplots(3, sharex = True, sharey = True)

X = np.random.randn(10000)

## 1:

ax1.hist(X, 50, normed = 1, facecolor = 'b', alpha = 0.75)
ax1.set_title('3 Boxplots')
ax1.axis([-3, 3, 0, .8])
ax1.set_title("boxplot 1")
ax1.set_xlabel("x label 1")
ax1.set_ylabel("y lable 1")

## 2:

ax2.hist(X, 100, normed = 1, facecolor = 'r', alpha = 0.75)
ax2.annotate('Maximun values', xy = (-0.2, .45), xytext = (0.2, 0.5),
             arrowprops = dict(facecolor = 'black', arrowstyle = '|-|'), )
ax2.axis([-3, 3, 0, .8])
ax2.grid(True)
ax2.set_title("boxplot 2")
ax2.set_xlabel("x label 2")
ax2.set_ylabel("y label 2")

## 3:

ax3.hist(X, 25, normed = 1, facecolor = 'r', alpha = 0.75)
ax3.annotate('Maximun', xy = (0, .45), xytext = (.3, 0.5),
             arrowprops = dict(facecolor = 'black', arrowstyle = 'fancy'), )
ax3.axis([-3, 3, 0, .8])
ax3.set_title("boxplot 3")
ax3.set_xlabel("x label 3")
ax3.set_ylabel("y label 3")

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace = 0.5)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible = False) # taking out xlabels except the last one if hspace = 0

plt.savefig('Histogram_example_11_estructure.png')

plt.show()


from numpy.random import normal, uniform


# Three subplots sharing both x/y axes
uniform_numbers = uniform(low = -3, high = 3, size = 1000)
print(len(uniform_numbers))
f, (ax1, ax2, ax3) = plt.subplots(3, sharex = True, sharey = True)

X = np.random.randn(10000)

## 1:

ax1.hist(X, 50, normed = 1, facecolor = 'b', alpha = 0.75)
ax1.set_title('3 Boxplots')
ax1.axis([-3, 3, 0, .8])
ax1.set_title("Gaussian")
ax1.set_xlabel("x label 1")
ax1.set_ylabel("y lable 1")

## 2:

ax2.hist(uniform_numbers, 100, normed = 1, facecolor = 'r', alpha = 0.75)
#ax2.axis([-3, 3, 0, .8])
ax2.grid(True)
ax2.set_title("Uniform")
ax2.set_xlabel("x label 2")
ax2.set_ylabel("y label 2")

## 3:

ax3.hist(X, bins = 100, histtype = 'stepfilled', normed = True, color = 'b', label = 'Gaussian')
ax3.hist(uniform_numbers, bins = 100, histtype = 'stepfilled', normed = True, color = 'r', label ='Uniform', alpha = 0.75)
ax3.legend()
ax3.axis([-3, 3, 0, .8])
ax3.set_title("Gaussian vs. uniform")
ax3.set_xlabel("x label 3")
ax3.set_ylabel("y label 3")

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace = 0.5)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible = False) # taking out xlabels except the last one if hspace = 0

plt.savefig('Histogram_example_11.png')

plt.show()