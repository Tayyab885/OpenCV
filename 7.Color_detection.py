import cv2
from cv2 import inRange
import numpy as np

def empty():
  pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
#So we are create a new window of TrackBars to select the colors
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",18,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",40,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",117,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

#First convert image to HSV Space
while True: #Using loop so that the colors of TrackBars keep on updating values
  img = cv2.imread("lambo.png")
  imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

  h_min = cv2.getTrackbarPos("Hue Min","TrackBars") #Remember put the same names as above
  h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
  s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
  s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
  v_min = cv2.getTrackbarPos("Val Min","TrackBars")
  v_max = cv2.getTrackbarPos("Val Max","TrackBars")
  
  #print(h_min,h_max,s_min,s_max,v_min,v_max)
  #Now we will use these values to filter our image to get that particular color
  #TO do that create a Mask and this is main part of color detection
  lower = np.array([h_min,s_min,v_min])
  upper = np.array([h_max,s_max,v_max])
  mask = cv2.inRange(imghsv,lower,upper)
  '''SO after running the mask change the values and keep the area you want to detect as white and than put those values above at cv2.createTracbar and than next time you run it will give you the masked image'''
  imgresult = cv2.bitwise_and(img,img,mask=mask)


  # cv2.imshow("Orignal Image",img)
  # cv2.imshow("HSV Image",imghsv)
  # cv2.imshow('Mask',mask)
  # cv2.imshow("Result",imgresult)
  imgstack = stackImages(0.6,([img,imghsv],[mask,imgresult]))
  cv2.imshow("Stacked Images",imgstack)
  cv2.waitKey(1)