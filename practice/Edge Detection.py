import cv2 
import numpy as np

#<======Reading The Image==========>
img = cv2.imread("src/CT-kidneys.jpeg")
# cv2.imshow("BGR",img)


#<====== Grayscale Image=========>
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# < ====== Laplacian =======>
lap = cv2.Laplacian(gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian",lap)

#<=====Sobel=====>
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1)

cv2.imshow("Sobel X",sobelx)
cv2.imshow("Sobel Y",sobely)

#<=======Combining the sobel image=======>

combined_sobel = cv2.bitwise_or(sobelx,sobely)
cv2.imshow("Sobel combine",combined_sobel)

#<========Canny Image=========>
canny = cv2.Canny(gray,150,175)
cv2.imshow("Canny",canny)


cv2.waitKey(0)