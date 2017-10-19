##
## Understanding the behavior of subplot I
## ==================================================
import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(10000)

'''
subplot(number of rows, number of columns, position of the element in the structure)
'''

plt.figure(1)                # the first figure

plt.subplot(321)
plt.plot(x, x)
plt.title('position 1')

plt.subplot(322)
plt.plot(x, x, color = 'r')
plt.title('position 2')

plt.subplot(323)
plt.plot(-x, -x, color = 'b')
plt.title('position 3')

plt.subplot(324)
plt.plot(-x, -x, color = 'r')
plt.title('position 4')

plt.subplot(325)
plt.plot(-x, -x, color = 'b')
plt.title('position 5')

plt.subplot(326)
plt.plot(-x, -x, color = 'r')
plt.title('position 6')

plt.subplots_adjust(hspace= 0.5)

plt.savefig('Histogram_example_12.png')

plt.show()

# source : https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate
