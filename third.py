#3. Reading the information of any particular image

import cv2
img=cv2.imread('2.jpg')
print(img.shape)

#1200-->height of the image in pixels
#1920-->width of the image in pixels
#3   -->channel value/channel number(RGB)[also called as depth]
