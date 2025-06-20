#5.GRAY SCALE SHORT PROGRAM

import cv2
img=cv2.imread('1.jpg',0) #0 here converts my image into grayscale

cv2.imshow('GRAY SCALE IMAGE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
