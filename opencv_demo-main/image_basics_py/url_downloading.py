import numpy as np
import urllib3
import cv2
from url_lib_func import url_to_image


# METHOD #1: OpenCV, NumPy, and urllib


url = "https://robotoai.com/wp-content/uploads/2020/11/cropped-logo-5.png"

print ("downloading %s" %(url))

image = url_to_image(url)

print ("downloaded 100%")

imgshow=cv2.imshow("Downloaded image", image)

cv2.imwrite ("/home/rubesh/our_logo.png", image)

print ("File saved")

cv2.waitKey(0)

