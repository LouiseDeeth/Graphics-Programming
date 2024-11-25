import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 3
ncols = 3
B = 0
G = 0
R = 255

img = cv2.imread('ATU1.jpg',)

gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)
cv2. waitKey(0) 
cv2. destroyAllWindows()

dst = cv2.cornerHarris(gray_image, 2, 3, 0.04) #corner harris of grayscale img
imgHarris = copy.deepcopy(img) #deep copy of the original img
 
# To plot the detected Harris corners, loop through every element in the 2d matrix –
# dst. If the element is greater than a threshold, draw a circle on the image as follows
threshold = 0.04; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(B, G, R),-1)

#plot multiple images
plt.subplot(nrows, ncols,1),plt.imshow(cv2. cvtColor(img, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,3),plt.imshow(cv2. cvtColor(imgHarris, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Harris Corners'), plt.xticks([]), plt.yticks([])
plt.show()