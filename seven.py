#resizing an image(scaling)
import cv2
import numpy as np

img=cv2.imread('1.jpg')
cv2.imshow('Original Image',img)
cv2.waitKey(500)

#case1: scale down
img1=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scale Down',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

#case2: ScaleUp
img2=cv2.resize(img,None,fx=1.5,fy=1.5)
cv2.imshow('Scale Up',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#case 3:Scaling_custom dimensions
img3=cv2.resize(img,(1000,400))
cv2.imshow('Scaling-Custom dimensions',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
