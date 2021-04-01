import cv2 as cv
import numpy as np 

img = cv.imread("src/image.jpeg")
cv.imshow("Dog",img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Dog Gray Image",gray)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow("BLURR Image",blur)

canny = cv.Canny(blur,125,175)
cv.imshow("Canny Image",canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresholded",thresh)

contours,hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contour drawn",blank)

cv.waitKey(0)
