from inspect import stack
import cv2
import numpy as np
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
  
def getContours(img): # It is to find the areas of the shapes
  contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
  for cnt in contours:
    area = cv2.contourArea(cnt)
    # print(area)
    # cv2.drawContours(imgcontours,cnt,-1,(255,0,0),3)
    if area > 500: # If to get the shapes of area >500
      cv2.drawContours(imgcontours,cnt,-1,(255,0,0),3)
      peri = cv2.arcLength(cnt,True) # To get the length
      # print(peri)
      approx = cv2.approxPolyDP(cnt,0.02*peri,True) # To get how many corners 
      # print(len(approx))
      #Now to get bounding box around the shapes
      objcorner = len(approx)
      x , y , w , h = cv2.boundingRect(approx)
      #Now lets guess the shapes
      if objcorner == 3:
        objectType = "Tri"
      elif objcorner == 4: #Now use aspratio to differtiate b/w rec and square
        aspratio = w/float(h)
        if aspratio > 0.95 and aspratio <1.05:
          objectType = "Square"
        else:
          objectType = "Rectangle"
      elif objcorner > 4:
        objectType = 'Circle'
      else:
        objectType = "None"
      cv2.rectangle(imgcontours,(x,y),(x+w,y+h),(0,255,0),2)
      cv2.putText(imgcontours,objectType,
                  (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
img = cv2.imread("shapes.png")
imgcontours = img.copy()
#First convert to gray scale and add blur
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgBlank = np.zeros_like(img)
#Use Canny edge detector
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
# cv2.imshow("Original",img)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
imgstack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgcontours,imgBlank]))
cv2.imshow("Images",imgstack)
cv2.waitKey(0)