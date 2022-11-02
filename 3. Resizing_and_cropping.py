import cv2
img = cv2.imread("me.jpeg")
'''
#Resizing Image
# print(img.shape) ##To check the size/shape of image and height come first than width
imgresize = cv2.resize(img,(480,640)) #and height come first than width
cv2.imshow("Image",imgresize)
cv2.waitKey(0)
'''
#Image Cropping
imgcropped = img[0:480,200:700]
cv2.imshow("Image",imgcropped)
cv2.waitKey(0)