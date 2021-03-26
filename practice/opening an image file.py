import cv2 as cv 

img = cv.imread("src/STScI-H-Massive-Stars-Engines-of-Creation-infographic-8000x4500.png")

cv.imshow("Cat",img)

cv.waitKey(0)
