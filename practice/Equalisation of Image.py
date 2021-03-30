import cv2

img = cv2.imread("Open CV/CT-kidneys.jpeg")

src = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dst = cv2.equalizeHist(src)

cv2.imshow("image",src)
cv2.imshow("Equalize image",dst)


cv2.waitKey(0)
