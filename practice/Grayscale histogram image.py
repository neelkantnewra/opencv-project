import cv2 
import matplotlib.pyplot as plt
import numpy as np 

img = cv2.imread("src/image.jpeg")
cv2.imshow("BGR",img)

# <=======creating blank image=====>

blank = np.zeros(img.shape[:2],dtype='uint8')

# <======Grayscale Image ===========>

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

#<======masking=======>
mask = cv2.circle(blank,(gray.shape[1]//2,gray.shape[0]//2 - 50 ),400,255,-1)
cv2.imshow("Mask",mask)

masked_image = cv2.bitwise_and(gray,gray,mask=mask)
cv2.imshow("masked Image",masked_image)

# <=========Grayscale Histogram=======>

# gray_hist = cv2.calcHist([gray],[0],None,[256],[0,255])
gray_hist = cv2.calcHist([gray],[0],mask,[256],[0,255])

# <========Ploting in Matplot==========>
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("bin")
plt.ylabel("Number of pixel") 
plt.plot(gray_hist)
plt.xlim([0,255])
plt.show()


cv2.waitKey()