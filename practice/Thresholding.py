import cv2 


#<======Reading The Image==========>
img = cv2.imread("src/image.jpeg")
# cv2.imshow("BGR",img)

#<====== Grayscale Image=========>
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# <====== Simple thresholding =========>

threshold , thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Image",thresh)

threshold , thresh_inv = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold  inverse Image",thresh_inv)

#<========= Adaptive Thresholding ===========>

adaptiv_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,0)
cv2.imshow("Adaptive Thresholding",adaptiv_thresh)

cv2.waitKey(0)