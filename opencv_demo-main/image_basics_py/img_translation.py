import cv2
import numpy
import imutils


img=cv2.imread("balloon.jpg")
img_translate=imutils.translate(img, 0, -210)
img_show=cv2.imshow("TRANSLATED_IMAGE", img_translate)
cv2.waitKey(0)
