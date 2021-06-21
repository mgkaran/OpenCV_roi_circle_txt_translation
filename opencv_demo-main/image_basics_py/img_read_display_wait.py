import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("baby.jpg")


#image properties
print(img.shape)
print(img.size)
print(img.dtype)


#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)