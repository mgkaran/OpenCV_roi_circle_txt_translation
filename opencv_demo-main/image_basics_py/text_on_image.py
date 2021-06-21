import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("dhoni.jpg")




# draw green text on the image
output = img.copy()
cv2.putText(output, "M S Dhoni", (625, 450),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 250, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


