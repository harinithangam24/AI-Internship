#5.binary image conversion (high contrast)
#first we convert the image into grayscale and then into binary

import cv2
img=cv2.imread('1.jpg',0)# 0 here converts the image into grayscale
cv2.imshow('gray scale image',img)
cv2.waitKey(2000)

ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#image is converted into binary
cv2.imshow('Binary',binary)#displays the binary image
cv2.waitKey()
cv2.destroyAllWindows()
