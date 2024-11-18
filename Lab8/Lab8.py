import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ATU.jpg',)

gray_image = cv2. cvtColor(img, cv2. COLOR_BGR2GRAY)
cv2. imshow('Original Image', img) cv2. imshow('Grayscale Image', gray_image)
cv2. waitKey(0) cv2. destroyAllWindows()
