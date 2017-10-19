'''
subplot(number of rows, number of columns, position of the element in the structure)
'''
import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(10000)

'''
subplot(number of rows, number of columns, position of the element in the structure)
'''

x_position = sum(x)/len(x)
y_position = sum(x)/len(x)

plt.figure(1)                # the first figure

plt.subplot(311)
plt.plot(x, x, color = 'g')
plt.title('position 1')
plt.text(x_position, y_position, 'coloreed text',
         verticalalignment = 'bottom', horizontalalignment = 'right',
         color = 'green', fontsize = 15)

plt.subplot(312)
plt.plot(x, x, color = 'white')
plt.title('position 2')
plt.text(x_position - 2, y_position + 1, r'HandShaking Lemma: $\sum_{v \in V} d(x) = 2 |E|$', fontsize = 10)
plt.text(x_position - 2, y_position - 1.5, u'Unicode characters: \374 \366', fontsize = 10)


plt.subplot(313)
plt.plot(-x, -x, color = 'r')
plt.title('position 3')
plt.annotate('Mean point', xy = (x_position, y_position), xytext = (x_position + 1, y_position - 1),
             arrowprops = dict(facecolor = 'black', shrink = 0.05))

plt.subplots_adjust(hspace = 0.5)

plt.savefig('Histogram_example_15.png')

plt.show()