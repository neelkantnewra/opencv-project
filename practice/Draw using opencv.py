import cv2 as cv 
import numpy as np 

# To create a blank image, 255 for keeping the intial  background white
blank = np.ones((500,500,3),dtype='uint8')*255

# 1.paint the image a certain color

blank[:] = 100,255,100   #changing background colour

# Draw a square box

blank[100:200,100:200] = 100,100,150

# 2. Draw a rectangle 

cv.rectangle(blank,(34,34),(250,250),(0,0,255),thickness=2)

# 3. Draw a circle
cv.circle(blank,(blank.shape[0]//3,blank.shape[1]//2),100,(0,0,255),thickness=2)

# 4. Draw a line

cv.line(blank,(80,80),(450,450),(0,0,0),thickness=10)
cv.line(blank,(450,80),(80,450),(0,0,0),thickness=10)


# 5. Write text 

cv.putText(blank,"Hello",(200,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255))

cv.imshow("Kidney",blank)

cv.waitKey(0)
