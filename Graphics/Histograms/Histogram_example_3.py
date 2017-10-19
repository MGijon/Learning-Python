# Basic histogram 3

import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)  # generating sample

hist, bins = np.histogram(x, bins=50)

width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2

plt.bar(center, hist, align = 'edge', width = width, color = ["red", "green", "blue", "violet"], edgecolor = ["red", "green"], linewidth = 0)


'''
color : scalar or array-like, optional
        the colors of the bar faces
        
edgecolor : scalar or array-like, optional
            the colors of the bar edges

align : {‘center’, ‘edge’}, optional, default: ‘center’.
        If ‘center’, interpret the x argument as the coordinates of the centers of the bars. 
        If ‘edge’, aligns bars by their left edges.
        To align the bars on the right edge pass a negative width and align = 'edge'.
        
linewidth : scalar or array-like, optional
            width of bar edge(s). If None, use default linewidth; If 0, don’t draw edges. default: None
'''

plt.show()