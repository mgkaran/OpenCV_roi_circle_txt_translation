import cv2
import imutils
import numpy

img=cv2.imread("baby.jpg")
imgshow=cv2.imshow("IMage", img)
cv2.waitKey(0) 

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvshow=cv2.imshow("HSV", hsv)
cv2.waitKey(0) 