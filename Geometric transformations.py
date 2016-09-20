# This program demonstrates example of geomertic 
# transformations, such as:
# - resizing
# - translation
# - rotation
# - affine transformation

import cv2
import numpy as np


# Resizing
img = cv2.imread('Images/lena.jpg')
res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resizing 0.5", res)
# OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resizing 2", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Translation
rows,cols = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Translation',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Rotation 90',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Affine transformation
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Affine', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Perspective transform
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('Perspective', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()