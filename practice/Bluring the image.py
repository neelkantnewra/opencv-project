import cv2 as cv 
import numpy as np 

#<========reading Image==========>

img = cv.imread("src/image.jpeg")
cv.imshow("Dog",img)

# <======== Averaging ============> 

average = cv.blur(img,(13,13))
cv.imshow("Mean Blur",average)

#<=========Gaussian blur ==========>

gaussian = cv.GaussianBlur(img,(13,13),0)
cv.imshow("Gaussian Blur",gaussian)

#<=========Median Blur ============>

median = cv.medianBlur(img,13)
cv.imshow("Median Blur",median)

# <==========Bilateral Blur=========>

bilateral = cv.bilateralFilter(img,55,35,25)
cv.imshow("Bilateral Blur",bilateral)


cv.waitKey(0)