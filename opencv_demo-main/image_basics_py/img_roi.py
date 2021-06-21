import cv2
import numpy
import imutils

#img read 
img=cv2.imread("balloon.jpg")



#eye_ROI
eye = img[310:382, 240:295]
img[50:122, 20:75] = eye



#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)