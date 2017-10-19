import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

#print(type(n))               # <class 'numpy.ndarray'>
#print(type(bins))            # <class 'numpy.ndarray'>
#print(type(patches))         # <class 'matplotlib.cbook.silent_list'>
#print(len(n))                # 50
#print(len(bins))             # 51

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.savefig('Histogram_example_6.png')


plt.show()





# source : https://matplotlib.org/devdocs/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
