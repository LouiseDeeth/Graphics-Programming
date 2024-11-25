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
