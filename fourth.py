#4.Gray scale image (BLACK AND WHITE IMAGE)

import cv2
img=cv2.imread('2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('ORIGINAL IMAGE',img) # displays the original image
cv2.imshow('GRAY SCALE IMAGE',gray) # displays the grray scale image

cv2.waitKey(0)
cv2.destroyAllWindows()
