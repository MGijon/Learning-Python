# Basic histogram 2

import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000) # generating sample

hist, bins = np.histogram(x, bins=50)

#print(type(hist))   # <class 'numpy.ndarray'>
#print(type(bins))   # <class 'numpy.ndarray'>
#print(len(hist))    # 50
#print(len(bins))    # 51

width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align = 'center', width = width)

'''
x : sequence of scalars
    the x coordinates of the bars.
    align controls if x is the bar center (default) or left edge.  -> parameter center
    
height : scalar or sequence of scalars
         the height(s) of the bars          -> parameter hist
         
align : {‘center’, ‘edge’}, optional, default: ‘center’.
        If ‘center’, interpret the x argument as the coordinates of the centers of the bars. 
        If ‘edge’, aligns bars by their left edges.
        To align the bars on the right edge pass a negative width and align = 'edge'.
        
width : scalar or array-like, optional
        the width(s) of the bars default: 0.8
'''

plt.show()