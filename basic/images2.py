import numpy as np
import cv2
import matplotlib.pyplot as plt

# if you don't have matplotlib please install matplotlib

img = cv2.imread('serabi-solo.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()