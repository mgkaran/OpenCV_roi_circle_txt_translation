import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("rubesh.jpg")


#image rotation with bound
rotate=imutils.rotate(img, 40)

#image rotation without bound
rotate_bound=imutils.rotate_bound(img, -60)



#image show
imgshow=cv2.imshow("Image",rotate)
cv2.waitKey(0)
imgshow=cv2.imshow("Image",rotate_bound)
cv2.waitKey(0)
