import cv2
import imutils
import numpy

img=cv2.imread("baby.jpg")
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0) 