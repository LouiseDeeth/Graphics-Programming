import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 1

img = cv2.imread('ATU.jpg',)

#single images
gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)
cv2. imshow('Original Image', img) 
cv2. imshow('Grayscale Image', gray_image)
cv2. waitKey(0) 
cv2. destroyAllWindows()

#multiple images
plt.subplot(nrows, ncols,1),plt.imshow(imgOrig, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()

imgOut = cv2.GaussianBlur(imgIn,(KernelSizeWidth, KernelSizeHeight),0)
