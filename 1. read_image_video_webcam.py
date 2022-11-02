import cv2
print("Package Imported")
'''
#Import Image
img = cv2.imread("me.jpeg")
cv2.imshow("Image",img)
cv2.waitKey(0)
'''
'''
#Import Video
cap =cv2.VideoCapture("alone.mkv")
# As video is sequence of images so we need while loop to go through each frames 
while True:
  success, img = cap.read() #Each frame of vid will store in img
  #Here success will tell whether the image is captured or not and return boolean
  cv2.imshow("Video",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
'''

# Import Webcam
cam = cv2.VideoCapture(0)
# cam.set(3, 1280)
# cam.set(4, 720) ##Set height and width
while True:
  success, img = cam.read()
  cv2.imshow("Webcam",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break