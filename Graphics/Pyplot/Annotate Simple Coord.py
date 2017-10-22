import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (3, 2))
an1 = ax.annotate("Test 1", xy = (0.5, 0.5), xycoords = "data",
                  va = "center", ha = "center",
                  bbox = dict(boxstyle = "round", fc = "w"))
an2 = ax.annotate("Test 2", xy = (1, 0.5), xycoords = an1,
                  xytext = (30, 0), textcoords = "offset points",
                  va = "center", ha = "left",
                  bbox = dict(boxstyle = "round", fc = "w"),
                  arrowprops = dict(arrowstyle = "->"))

plt.savefig("Annotate_Simple_Coord_a.png")

plt.show()

# source 1 : https://matplotlib.org/devdocs/gallery/userdemo/annotate_simple_coord01.html#sphx-glr-gallery-userdemo-annotate-simple-coord01-py

## =====================================

import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize = (3, 2))
an1 = ax.annotate("Test 1", xy = (0.5, 0.5), xycoords = "data",
                  va = "center", ha = "center",
                  bbox = dict(boxstyle = "round", fc = "w"))

an2 = ax.annotate("Test 2", xy = (0.5, 1.), xycoords = an1,
                  xytext = (0.5, 1.1), textcoords = (an1, "axes fraction"),
                  va = "bottom", ha = "center",
                  bbox = dict(boxstyle = "round", fc = "w"),
                  arrowprops = dict(arrowstyle = "->"))

fig.subplots_adjust(top = 0.83)

plt.savefig("Annotate_Simple_Coord_b.png")

plt.show()

# source 2 : https://matplotlib.org/devdocs/gallery/userdemo/annotate_simple_coord02.html#sphx-glr-gallery-userdemo-annotate-simple-coord02-py

## =====================================

import matplotlib.pyplot as plt
from matplotlib.text import OffsetFrom


fig, ax = plt.subplots(figsize = (3, 2))
an1 = ax.annotate("Test 1", xy = (0.5, 0.5), xycoords = "data",
                  va = "center", ha = "center",
                  bbox = dict(boxstyle = "round", fc = "w"))

offset_from = OffsetFrom(an1, (0.5, 0))
an2 = ax.annotate("Test 2", xy = (0.1, 0.1), xycoords = "data",
                  xytext = (0, -10), textcoords = offset_from,
                  # xytext is offset points from "xy = (0.5, 0), xycoords = an1"
                  va = "top", ha = "center",
                  bbox = dict(boxstyle = "round", fc = "w"),
                  arrowprops = dict(arrowstyle = "->"))

plt.savefig("Annotate_Simple_Coord_c.png")

plt.show()

# source 3 : https://matplotlib.org/devdocs/gallery/userdemo/annotate_simple_coord03.html#sphx-glr-gallery-userdemo-annotate-simple-coord03-py