import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('bug.png') 				# la importamos como un array de numpy

#print(np.shape(img))						# -> (375, 500, 3): 375 columnas con 500 filas y tres colores po cada una

lum_img = img[:,:,0]


plt.subplot(221)
plt.imshow(img)

plt.subplot(222)
plt.imshow(lum_img)

plt.subplot(223)
plt.imshow(lum_img, cmap = "hot")

plt.subplot(224)
plt.imshow(lum_img, cmap = 'nipy_spectral')
plt.colorbar()

plt.savefig("Playing_with_bug.png")

plt.show()


# source : https://matplotlib.org/users/image_tutorial.html