import cv2
import numpy as np
img = cv2.imread('me.jpeg')
'''
#Convert image to grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage",imgGray)
cv2.waitKey(0)
'''

'''
#Convert to Blur Image
imgBlur = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)
'''

'''
# Edge Detector image
imgcanny = cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgcanny)
cv2.waitKey(0)
'''

# Image Dialation
imgcanny = cv2.Canny(img,100,100)
kernel = np.ones((5,5),np.uint8)
imgdialation = cv2.dilate(imgcanny,kernel,iterations=1)


# Image Erosion
imgEroded = cv2.erode(imgdialation,kernel,iterations=1)
cv2.imshow("Image Dialation",imgEroded)
cv2.waitKey(0)
# Note Canny, Dialation and Erotion work together and almost same
