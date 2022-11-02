import cv2
import numpy as np
img = cv2.imread("cards.jpg")

width,height = 250,350 #output image size
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #dimesions of image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # postion of above
matrix  = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Cards",img)
cv2.imshow("Output",imgoutput)
cv2.waitKey(0)