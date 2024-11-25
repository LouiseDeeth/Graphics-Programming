import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 3

#load the image
#img = cv2.imread('ATU1.jpg',)
img = cv2.imread('OperaHouse.jpg',)

# convert to grayscale
gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)

#Harris corner detection
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04) #corner harris of grayscale img
imgHarris = copy.deepcopy(img) #deep copy of the original img

B, G, R = 0, 0, 255 # red colour for marking the corners
# To plot the detected Harris corners, loop through every element in the 2d matrix –
# dst. If the element is greater than a threshold, draw a circle on the image as follows
threshold = 0.04; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(B, G, R),-1)

# Shi Tomasi algorithm
maxCorners = 50 #the number of corners to be detected
qualityLevel = 0.01 # minimum accepted quality of corners
minDistance = 10 # minimum distance between corners

corners = cv2.goodFeaturesToTrack(gray_image,maxCorners,qualityLevel,minDistance) 
corners = np.int0(corners)  #convert corners values to integer 

# create another deep copy
imgShiTomasi = copy.deepcopy(img) #deep copy of the original img

B, G, R = 255, 0, 0 # blue colour for marking the corners
for i in corners: 
    x,y = i.ravel() 
    cv2.circle(imgShiTomasi,(x,y),3,(B, G, R),-1) 

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)
 
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
 
# draw only keypoints location,not size and orientation
imgORB = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0) # green colour

#plot multiple images
plt.figure(figsize=(10, 8))
plt.subplot(nrows, ncols,1),plt.imshow(cv2. cvtColor(img, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,3),plt.imshow(cv2. cvtColor(imgHarris, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Harris Corners'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,4),plt.imshow(cv2. cvtColor(imgShiTomasi, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('Shi Tomasi Corners'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,5),plt.imshow(cv2. cvtColor(imgORB, cv2. COLOR_BGR2RGB), cmap = 'gray')
plt.title('ORB Key Features'), plt.xticks([]), plt.yticks([])

plt.show()