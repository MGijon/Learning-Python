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

plt.subplot(221)
plt.plot(x, x, color = 'g')
plt.title('position 1')
plt.text(x_position, y_position, "style: italic", style = 'italic', bbox = {'facecolor': 'red', 'alpha':0.5, 'pad':10})

plt.subplot(222)
plt.plot(x, x, color = 'g')
plt.title('position 2')
plt.text(x_position, y_position, "style: normal", style = 'normal', bbox = {'facecolor': 'green', 'alpha':0.5, 'pad':10})


plt.subplot(223)
plt.plot(-x, -x, color = 'r')
plt.title('position 3')
plt.text(x_position, y_position, "style: oblique", style = 'oblique', bbox = {'facecolor': 'yellow', 'alpha':0.5, 'pad':10})


plt.subplot(224)
plt.plot(-x, -x, color = 'r')
plt.title('position 4')
plt.text(x_position, y_position, "style: oblique", style = 'oblique', bbox = {'facecolor': 'violet', 'alpha':0.5, 'pad':10})




plt.subplots_adjust(hspace = 0.5)

plt.savefig('Histogram_example_14.png')

plt.show()