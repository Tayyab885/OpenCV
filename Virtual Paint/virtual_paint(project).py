import cv2 as cv
import numpy as np 

# Read the webcam
cap = cv.VideoCapture(0)
frame_width = 640
frame_height = 480
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,140) #set webcam brightnes

colors = [[0,109,0,19,255,255],[45,52,0,116,255,255],[67,45,0,179,255,255]]
color_values = [[52,51,255],[0,153,0],[255,51,51]]
my_points = [] #x,y,colorId

# Color Detection
def color_detection(img,colors,color_values):
  img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
  count = 0
  newpoints = []
  for c in colors:
    lower = np.array(c[0:3])
    upper = np.array(c[3:6])
    mask = cv.inRange(img_hsv,lower,upper)
    # cv.imshow("Image",mask)
    x,y = getContours(mask)
    cv.circle(imgresult,(x,y),10,(255,0,0),cv.FILLED)
    if x!=0 and y!=0:
      newpoints.append([x,y,count])
    count+=1
  return newpoints
# Get Contours to see where the object in the window
def getContours(img): # It is to find the areas of the shapes
  contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
  x,y,w,h = 0,0,0,0
  for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 500: # If to get the shapes of area >500
      #cv.drawContours(imgresult,cnt,-1,(255,0,0),3)
      peri = cv.arcLength(cnt,True) # To get the length
      approx = cv.approxPolyDP(cnt,0.02*peri,True) # To get how many corners 
      x , y , w , h = cv.boundingRect(approx)
  return x+w//2,y

def draw(my_points,color_values):
  for point in my_points:
    cv.circle(imgresult,(point[0],point[1]),10,color_values[point[2]],cv.FILLED)


while True:
  x, img = cap.read()
  imgresult = img.copy()
  newpoints = color_detection(img,colors,color_values)
  if len(newpoints) != 0:
    for p in newpoints:
      my_points.append(p)
  if len(my_points)!=0:
    draw(my_points,color_values)
  cv.imshow("Webcam",imgresult)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break