import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)                # the first figure

## subplot( 'number of rows', 'number of columns', 'curret possition in this structure')

plt.subplot(211)             # the first subplot in the first figure

x = np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed = 1, facecolor = 'b', alpha = 0.75)
plt.title('Normal Distribution')
plt.axis([-3, 3, 0, .8])
plt.grid(True)

plt.annotate('max', xy = (0, 0.45), xytext = (0.3, 0.55),
             arrowprops = dict(facecolor = 'black', arrowstyle = 'simple'), )


plt.subplot(212)             # the second subplot in the first figure

x = np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed = 1, facecolor = 'red', alpha = 0.75)

plt.annotate('fancy', xy = (1, .2), xytext = (1.3, 0.25),
             arrowprops = dict(facecolor = 'black', arrowstyle = 'fancy'), )

plt.annotate('wedge', xy = (0, 0.25), xytext = (0.3, 0.35),
             arrowprops = dict(facecolor = 'black', arrowstyle = 'wedge'), )

plt.annotate('simple', xy = (3, 0.1), xytext = (3.3, 0.20),
             arrowprops = dict(facecolor = 'black', arrowstyle = 'simple'), )

plt.annotate('-', xy = (-4., .1), xytext = (-3.7, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '-'), )

plt.annotate('->', xy = (-4., 2.5), xytext = (-3.7, 2.3),
             arrowprops = dict(facecolor = 'black', arrowstyle = '->'), )

plt.annotate('<-', xy = (-2., 0.3), xytext = (-1.7, 0.4),
             arrowprops = dict(facecolor = 'black', arrowstyle = '<-'), )

plt.annotate('<->', xy = (0., 0.1), xytext = (0.3, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '<->'), )

plt.annotate('-|>', xy = (2, 0.30), xytext = (2.3, 0.4),
             arrowprops = dict(facecolor = 'black', arrowstyle = '-|>'), )

plt.annotate('<|-', xy = (1.1, 0.10), xytext = (1.4, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '<|-'), )

plt.annotate('<|-|>', xy = (-3., 0.25), xytext = (-3.3, 0.35),
             arrowprops = dict(facecolor = 'black', arrowstyle = '<|-|>'), )

plt.annotate('|-|', xy = (-1.5, 0.1), xytext = (-1.2, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '|-|'), )

plt.annotate('|-|', xy = (-1.5, 0.1), xytext = (-1.2, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '|-|'), )

plt.annotate('-[', xy = (-2.5, 0.1), xytext = (-2.2, 0.2),
             arrowprops = dict(facecolor = 'black', arrowstyle = '-['), )

plt.annotate('<-', xy = (3., 0.25), xytext = (3.2, 0.30),
             arrowprops = dict(facecolor = 'black', arrowstyle = '<-'), )

plt.title('9 kinds of arrows')

plt.savefig('Histogram_example_8.png')

plt.show()




# source : https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate
