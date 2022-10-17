import cv2

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
  x,img = cap.read()
  # img = cv2.imread("resize.jpg")
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = faceCascade.detectMultiScale(img_gray,1.2,4)
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
  cv2.imshow("Webcam",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()