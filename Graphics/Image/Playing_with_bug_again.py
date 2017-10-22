import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('bug.png')
lum_img = img[:,:,0]


plt.hist(lum_img.ravel(), bins = 256, range = (0.0, 1.0), fc = 'k', ec = 'k')

plt.savefig("Playing_with_bug_again_histogram.png")

plt.show()

## =================================

'''
orientation : [None|’vertical’|’horizontal’]
              The orientation of the colorbar. Typically, this keyword shouldn’t be used, as it can be derived
              from the location keyword.
'''

plt.subplot(121)

plt.imshow(lum_img)
plt.colorbar(orientation = 'horizontal')
plt.title('Before')

plt.subplot(122)

plt.imshow(lum_img, clim=(0.0, 0.7))
plt.colorbar(orientation = 'horizontal')
plt.title('After')

plt.savefig("Playing_with_bug_again.png")

plt.show()

## =================================

##
##  Interpolations
## =================================

from PIL import Image

img = Image.open('bug.png')
img.thumbnail((64, 64), Image.ANTIALIAS) # resizes image in-place
imgplot = plt.imshow(img)
plt.title('Default interpolation')
plt.savefig("Playing_with_bug_again_Default_interpolation.png")

plt.show()

imgplot = plt.imshow(img, interpolation = "nearest")
plt.title('Nearest interpolation')
plt.savefig("Playing_with_bug_again_Nearest_interpolation.png")

plt.show()

imgplot = plt.imshow(img, interpolation = "bicubic")
plt.title('Bicubic interpolation')
plt.savefig("Playing_with_bug_again_Bicubic_interpolation.png")

plt.show()

# source : https://matplotlib.org/users/image_tutorial.html