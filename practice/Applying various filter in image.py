import cv2 as cv 
import numpy as np 

img = cv.imread("src/Picture27.png")

#gray image
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",gray_image) 

#blurr image
blur_image = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blurr Image",blur_image) 

#Edge cascade

edge_image = cv.Canny(img,100,600)
cv.imshow("Canny image",edge_image)

# Dilating the image

dilated_image = cv.dilate(edge_image,(3,3),iterations=2)
cv.imshow("Dilated",dilated_image) 

# Eroding to get almost  original image

erode_image = cv.erode(dilated_image,(3,3),iterations=2)
cv.imshow("Eroded",erode_image) 

# Resize

resize_image = cv.resize(img,(1000,1000),interpolation = cv.INTER_CUBIC)
cv.imshow("resize",resize_image) 

resize_image_l = cv.resize(img,(1000,1000),interpolation = cv.INTER_LINEAR)
cv.imshow("resizel",resize_image_l) 

# Croping 
cropped_image = resize_image_l[200:600,600:900]
cv.imshow("cropped",cropped_image) 


cv.waitKey(0)
