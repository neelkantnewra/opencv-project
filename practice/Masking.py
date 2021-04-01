import cv2 as cv 
import numpy as np 

#<========reading Image==========>

img = cv.imread("src/image.jpeg")
cv.imshow("Dog",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank",blank)

#<======== Cicle Mask ===========>

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2 - 50 ),400,255,-1)
cv.imshow("Mask",mask)

# <======= Lovely Mask ===========>
rectangle = cv.rectangle(blank,(img.shape[1]//2 -50 ,img.shape[0]//2 -50),(img.shape[1]//2 +50,img.shape[0]//2+50),255,-1)
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),img.shape[1]//3,255,-1)

bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR",bitwise_or)
#<======== Masked Image ==========>

masked_image = cv.bitwise_and(img,img,mask=bitwise_or)
cv.imshow("Masked Image",masked_image)

cv.waitKey(0)