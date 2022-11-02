import cv2
import numpy as np

#img = np.zeros((512,512)) # Image of zeros is black
#img = np.ones((512,512)) # Image of ones will be white

img = np.zeros((512,512,3),np.uint8) # now to color image
#img[:] = 255,0,0

#Create lines
#cv2.line(img,(0,0),(300,300),(0,255,0),3)
#for line on whole image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#Create rectangles
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#to fill rectangle with color use cv2.FIlled at place of 2

# Create circle
cv2.circle(img,(450,50),50,(255,255,0),5)

# Put text on Images
cv2.putText(img,"OpenCV",(300,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)
cv2.waitKey(0) 