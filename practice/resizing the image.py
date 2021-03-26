import cv2 as cv 

img = cv.imread("src/STScI-H-Massive-Stars-Engines-of-Creation-infographic-8000x4500.png")



def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

img = rescaleFrame(img)

cv.imshow("Cat",img)

cv.waitKey(0)
