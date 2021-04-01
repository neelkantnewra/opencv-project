import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread("src/image.jpeg")
cv.imshow("Dog",img)




#GRay image

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Dog Gray Image",gray)

#BGR TO HSV

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("Dog HSV Image",hsv)

# HSV to bgr

bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow("Dog BGR Image",bgr)

#BGR to LAB 

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("Dog LAB Image",lab)

#BGR to RBG

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("Dog RGB Image",rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
