import cv2 
import matplotlib.pyplot as plt
import numpy as np 

#<======Reading The Image==========>
img = cv2.imread("src/image.jpeg")
cv2.imshow("BGR",img)

#<========Creating Blank Image=======>
blank = np.zeros(img.shape[:2],dtype='uint8')

#<=========Creating Mask of circle=====>

circle = cv2.circle(blank,(img.shape[1]//2  + 60,img.shape[0]//2 - 50),400,255,-1)
cv2.imshow("Circle" , circle)
 
#<======Applying Mask on Img============>
mask = cv2.bitwise_and(img,img,mask=circle)
cv2.imshow("Masked Image",mask)

#<========Creating Color Histogram======>
plt.figure()
plt.title("Color Histogram Histogram")
plt.xlabel("bin")
plt.ylabel("Number of pixel") 
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv2.calcHist([img],[i],circle,[256],[0,256])  #Here we use Circle as mask
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.show()
cv2.waitKey()