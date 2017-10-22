import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize = (3, 3))

ax.annotate("",
            xy = (0.2, 0.2), xycoords = 'data',
            xytext = (0.8, 0.8), textcoords = 'data',
            arrowprops = dict(arrowstyle = "->",
                            connectionstyle = "arc3"),
            )

plt.savefig("Annotate_Simple_a.png")

plt.show()

## ====================

fig, ax = plt.subplots(figsize = (3, 3))

ax.annotate("Test",
            xy = (0.2, 0.2), xycoords = 'data',
            xytext = (0.8, 0.8), textcoords = 'data',
            size = 20, va = "center", ha = "center",
            arrowprops = dict(arrowstyle = "simple",
                            connectionstyle = "arc3,rad=-0.2"),
            )

plt.savefig("Annotate_Simple_b.png")

plt.show()

## ====================

fig, ax = plt.subplots(figsize = (3, 3))

ann = ax.annotate("Test",
                  xy = (0.2, 0.2), xycoords = 'data',
                  xytext = (0.8, 0.8), textcoords = 'data',
                  size = 20, va = "center", ha = "center",
                  bbox = dict(boxstyle = "round4", fc = "w"),
                  arrowprops = dict(arrowstyle = "-|>",
                                  connectionstyle = "arc3,rad=-0.2",
                                  fc = "w"),
                  )

plt.savefig("Annotate_Simple_c.png")

plt.show()



# source 1 : https://matplotlib.org/gallery/userdemo/annotate_simple01.html
# source 2 : https://matplotlib.org/devdocs/gallery/userdemo/annotate_simple02.html
# source 3 : https://matplotlib.org/devdocs/gallery/userdemo/annotate_simple03.html#sphx-glr-gallery-userdemo-annotate-simple03-py