import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (150, 160, 146, 172, 155)
menStd = (20, 30, 32, 10, 20)

fig, ax = plt.subplots()

ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
p1 = ax.bar(ind, menMeans, width, color = 'r', bottom = 0, yerr = menStd)


womenMeans = (145, 149, 172, 165, 200)
womenStd = (30, 25, 20, 31, 22)
p2 = ax.bar(ind + width, womenMeans, width,
            color = 'y', bottom = 0, yerr = womenStd)

ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((p1[0], p2[0]), ('Men', 'Women'))
ax.autoscale_view()

plt.savefig("Barchart_with_lines_and_legends.png")

# source : https://matplotlib.org/devdocs/gallery/units/bar_unit_demo.html#sphx-glr-gallery-units-bar-unit-demo-py

plt.show()