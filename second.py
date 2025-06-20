#2. Create a duplicate image of any extension

import cv2
img = cv2.imread('1.jpg')# reading the image
cv2.imshow('Output 1',img)#displaying the image

cv2.imwrite('harini.png',img) #creating a duplicate image with different extension

cv2.waitKey(0)
cv2.destroyAllWindows()
