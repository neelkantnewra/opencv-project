import cv2 as cv 
import numpy as np

img = cv.imread("Open CV/CT-kidneys.jpeg")

cv.imshow("Image",img)

# Translation
def translate(image,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (image.shape[1],image.shape[0])
    return cv.warpAffine(image,transMat,dimension)

#   -x -----> shifting left
#   -y -----> shifting up
#    x -----> shifting right
#    y -----> shifting down


translated = translate(img,-50,-50)
cv.imshow("translate",translated)

# Rotation
 
def rotate(image,angle,rotationPoint=None):
    (height,width) = image.shape[:2]
    if rotationPoint == None:
        rotationPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotationPoint,angle,1.0)
    dimension = (width,height)
    return cv.warpAffine(image,rotMat,dimension)


rotated_image = rotate(img,-45)
cv.imshow("Rotated",rotated_image)

rotated_image_r = rotate(rotated_image,45)
cv.imshow("Rotated_r",rotated_image_r)
    
# Resizing Image 

resized = cv.resize(img,(1000,800),interpolation= cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Fliping Image

#  0 -----> verticle flipping
#  1 -----> Horizontal flipping
# -1 -----> Both Horizontal and Verticle flipping

flip = cv.flip(img,-1)
cv.imshow("Flipped",flip)

cv.waitKey(0)
