import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 3
ncols = 3

img = cv2.imread('ATU1.jpg',)

gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)
cv2. waitKey(0) 
cv2. destroyAllWindows()

dst = cv2.cornerHarris(img, 2, 3, 0.04)
imgHarris = copy.deepcopy(dst) 
 
threshold = 0.9; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(255, 243, 0),-1)

