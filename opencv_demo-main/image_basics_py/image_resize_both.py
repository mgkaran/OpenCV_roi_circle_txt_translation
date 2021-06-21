import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("baby.jpg")


#normal resize(aspect ration not preserved)
resize=cv2.resize(img,(1000,500))

#imutils resize (preserves the aspect ration)
resize_imutils = imutils.resize(img,width=100)


#image show
imgshow=cv2.imshow("Image", resize)
cv2.waitKey(0)
imgshow=cv2.imshow("Image", resize_imutils)
cv2.waitKey(0)
