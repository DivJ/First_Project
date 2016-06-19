from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
img=mpimg.imread('stinkbug.png')
print img
plt.imshow(img)
plt.show()
plt.imshow(img[:,:,0], cmap="Accent")
plt.show()
plt.imshow(img, cmap="Accent")
plt.show() 
plt.imshow(img[:,:,0], cmap="Greys")
plt.show()
            