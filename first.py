# read the image

import cv2 #we are importing the opencv/computer vision library
img=cv2.imread('1.jpg') # we are reading the image and storing it inside the img variable
cv2.imshow('Output 1' , img) #here we are displaying the image

cv2.waitKey(0)
cv2.destroyAllWindows() #if in case  of the windows is not closed,this ine will make sure all the windows are destroyed before the execution of the program

#Output 1 --> image window name
#cv2.waitKey(0)--> makes the image stay forever
#cv2.waitKey(3000)--> makes the image stay only for 3 seconds
