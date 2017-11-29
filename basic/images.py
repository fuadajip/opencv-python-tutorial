import numpy as np
import cv2

# load color image in grayscale mode
img = cv2.imread('serabi-solo.jpg')
img_gray = cv2.imread('serabi-solo.jpg',0)

# displaying image
cv2.imshow('window name', img_gray)

# displaying image with resizeable window
cv2.namedWindow('window name 2', cv2.WINDOW_NORMAL)
cv2.imshow('window name 2', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit

    # use this to write image
    cv2.imwrite('another_serabi.png',img)
    cv2.destroyAllWindows()