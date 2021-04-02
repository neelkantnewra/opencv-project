import cv2

#<=========Reading The Image===========>
img = cv2.imread("src/group-young-teenage-girls-together-nature_21730-5450.jpeg")
cv2.imshow("BGR",img)

#<========= GrayScale Image============>
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

#<=========Reading model==============>

haar_cascade = cv2.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray,1.1,6)

# print(f"Number of faces found: {len(faces_rect)}")

#ploting Rectangle on the detected face
for (x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+h,y+h),(0,255,0),2)

cv2.imshow("Detected Face",img)


cv2.waitKey(0)
