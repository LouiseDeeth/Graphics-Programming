import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 2

img = cv2.imread('ATU.jpg',)

#single images
gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)
#cv2. imshow('Original Image', img) 
#cv2. imshow('Grayscale Image', gray_image)
cv2. waitKey(0) 
cv2. destroyAllWindows()

#plot multiple images
plt.subplot(nrows, ncols,1),plt.imshow(cv2. cvtColor(img, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()

imgOut = cv2.GaussianBlur(img,(3, 3),0)
imgOut = cv2.GaussianBlur(img,(9, 9),0)