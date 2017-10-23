from matplotlib.path import Path


def custom_box_style(x0, y0, width, height, mutation_size, mutation_aspect=1):
    """
    Given the location and size of the box, return the path of
    the box around it.

     - *x0*, *y0*, *width*, *height* : location and size of the box
     - *mutation_size* : a reference scale for the mutation.
     - *aspect_ratio* : aspect-ration for the mutation.
    """

    # note that we are ignoring mutation_aspect. This is okay in general.

    # padding
    mypad = 0.3
    pad = mutation_size * mypad

    # width and height with padding added.
    width = width + 2 * pad
    height = height + 2 * pad

    # boundary of the padded box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height

    cp = [(x0, y0),
          (x1, y0), (x1, y1), (x0, y1),
          (x0-pad, (y0+y1)/2.), (x0, y0),
          (x0, y0)]

    com = [Path.MOVETO,
           Path.LINETO, Path.LINETO, Path.LINETO,
           Path.LINETO, Path.LINETO,
           Path.CLOSEPOLY]

    path = Path(cp, com)

    return path


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (3, 3))
ax.text(0.5, 0.5, "Test", size = 30, va = "center", ha = "center",
        bbox = dict(boxstyle = custom_box_style, alpha = 0.2))

plt.savefig("Custom_Boxes_a.png")

plt.show()

## =========================================

from matplotlib.patches import BoxStyle
import matplotlib.pyplot as plt


# we may derive from matplotlib.patches.BoxStyle._Base class.
# You need to override transmute method in this case.

class MyStyle(BoxStyle._Base):
    """
    A simple box.
    """

    def __init__(self, pad=0.3):
        """
        The arguments need to be floating numbers and need to have
        default values.

         *pad*
            amount of padding
        """

        self.pad = pad
        super(MyStyle, self).__init__()

    def transmute(self, x0, y0, width, height, mutation_size):
        """
        Given the location and size of the box, return the path of
        the box around it.

         - *x0*, *y0*, *width*, *height* : location and size of the box
         - *mutation_size* : a reference scale for the mutation.

        Often, the *mutation_size* is the font size of the text.
        You don't need to worry about the rotation as it is
        automatically taken care of.
        """

        # padding
        pad = mutation_size * self.pad

        # width and height with padding added.
        width, height = width + 2.*pad, \
                        height + 2.*pad,

        # boundary of the padded box
        x0, y0 = x0-pad, y0-pad,
        x1, y1 = x0+width, y0 + height

        cp = [(x0, y0),
              (x1, y0), (x1, y1), (x0, y1),
              (x0-pad, (y0+y1)/2.), (x0, y0),
              (x0, y0)]

        com = [Path.MOVETO,
               Path.LINETO, Path.LINETO, Path.LINETO,
               Path.LINETO, Path.LINETO,
               Path.CLOSEPOLY]

        path = Path(cp, com)

        return path


# register the custom style
BoxStyle._style_list["angled"] = MyStyle

fig, ax = plt.subplots(figsize = (3, 3))
ax.text(0.5, 0.5, "Test", size = 30, va = "center", ha = "center", rotation = 30,
        bbox = dict(boxstyle = "angled,pad = 0.5", alpha = 0.2))

del BoxStyle._style_list["angled"]

plt.savefig("Custom_Boxes_b.png")

plt.show()


# source 1 : https://matplotlib.org/gallery/userdemo/custom_boxstyle01.html
# source 2 : https://matplotlib.org/devdocs/gallery/userdemo/custom_boxstyle02.html#sphx-glr-gallery-userdemo-custom-boxstyle02-py