import matplotlib.pyplot as plt

##
##  Example 1:
##  ==========



def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va = "center", ha = "center")
        ax.tick_params(labelbottom = False, labelleft = False)


fig = plt.figure(0)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan = 3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan = 2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan = 2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

fig.suptitle("subplot2grid")
make_ticklabels_invisible(fig)

plt.savefig('Gridspec_example_1.png')
plt.show()

# source : https://matplotlib.org/gallery/userdemo/demo_gridspec01.html


##
##  Example 2:
##  ==========


from matplotlib.gridspec import GridSpec


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


fig = plt.figure()

gs = GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])

fig.suptitle("GridSpec")
make_ticklabels_invisible(fig)

plt.savefig('Gridspec_example_2.png')
plt.show()


# source : https://matplotlib.org/gallery/userdemo/demo_gridspec02.html#sphx-glr-gallery-userdemo-demo-gridspec02-py


##
##  Example 3:
##  ==========


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


# demo 3 : gridspec with subplotpars set.

fig = plt.figure()

fig.suptitle("GridSpec w/ different subplotpars")

gs1 = GridSpec(3, 3)
gs1.update(left = 0.05, right = 0.48, wspace = 0.05)
ax1 = plt.subplot(gs1[:-1, :])
ax2 = plt.subplot(gs1[-1, :-1])
ax3 = plt.subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3)
gs2.update(left = 0.55, right = 0.98, hspace = 0.05)
ax4 = plt.subplot(gs2[:, :-1])
ax5 = plt.subplot(gs2[:-1, -1])
ax6 = plt.subplot(gs2[-1, -1])

make_ticklabels_invisible(fig)

plt.savefig('Gridspec_example_3.png')
plt.show()


# source : https://matplotlib.org/gallery/userdemo/demo_gridspec03.html#sphx-glr-gallery-userdemo-demo-gridspec03-py


##
##  Example 4:
##  ==========


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va = "center", ha = "center")
        ax.tick_params(labelbottom = False, labelleft = False)


# gridspec inside gridspec

f = plt.figure()

gs0 = gridspec.GridSpec(1, 2)

gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec = gs0[0])

ax1 = plt.Subplot(f, gs00[:-1, :])
f.add_subplot(ax1)
ax2 = plt.Subplot(f, gs00[-1, :-1])
f.add_subplot(ax2)
ax3 = plt.Subplot(f, gs00[-1, -1])
f.add_subplot(ax3)


gs01 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec = gs0[1])

ax4 = plt.Subplot(f, gs01[:, :-1])
f.add_subplot(ax4)
ax5 = plt.Subplot(f, gs01[:-1, -1])
f.add_subplot(ax5)
ax6 = plt.Subplot(f, gs01[-1, -1])
f.add_subplot(ax6)

plt.suptitle("GridSpec Inside GridSpec")
make_ticklabels_invisible(f)

plt.savefig('Gridspec_example_4.png')
plt.show()


# soure : https://matplotlib.org/gallery/userdemo/demo_gridspec04.html#sphx-glr-gallery-userdemo-demo-gridspec04-py



##
##  Example 5:
##  ==========


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va = "center", ha = "center")
        ax.tick_params(labelbottom = False, labelleft = False)


f = plt.figure()

gs = gridspec.GridSpec(2, 2, width_ratios = [1, 2], height_ratios = [4, 1])

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])

make_ticklabels_invisible(f)

plt.savefig('Gridspec_example_5.png')
plt.show()


# source : https://matplotlib.org/gallery/userdemo/demo_gridspec05.html#sphx-glr-gallery-userdemo-demo-gridspec05-py



##
##  Example 6:
##  ==========


import numpy as np
from itertools import product


def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)


fig = plt.figure(figsize=(8, 8))

# gridspec inside gridspec
outer_grid = gridspec.GridSpec(4, 4, wspace=0.0, hspace=0.0)

for i in range(16):
    inner_grid = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec = outer_grid[i], wspace = 0.0, hspace = 0.0)
    a = i // 4 + 1
    b = i % 4 + 1
    for j, (c, d) in enumerate(product(range(1, 4), repeat = 2)):
        ax = plt.Subplot(fig, inner_grid[j])
        ax.plot(*squiggle_xy(a, b, c, d))
        ax.set_xticks([])
        ax.set_yticks([])
        fig.add_subplot(ax)

all_axes = fig.get_axes()

#show only the outside spines
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
    if ax.is_first_row():
        ax.spines['top'].set_visible(True)
    if ax.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ax.is_first_col():
        ax.spines['left'].set_visible(True)
    if ax.is_last_col():
        ax.spines['right'].set_visible(True)

plt.savefig('Gridspec_example_6.png')
plt.show()

# source : https://matplotlib.org/gallery/userdemo/demo_gridspec06.html