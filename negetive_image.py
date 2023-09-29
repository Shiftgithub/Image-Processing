# Mamun Mia Turan
# ID : CSE2001019039
import numpy as np
import cv2

img = cv2.imread('images/lena.jpg')

# img = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image', img)

# Calculate the negative image by subtracting each pixel value from 255
negative_img = 255 - img

cv2.imshow('negative image', negative_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
