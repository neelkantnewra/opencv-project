import numpy as np 
import cv2 

haar_cascade = cv2.CascadeClassifier("Face Recogination/haar_face.xml") 
characters = ["Loki","Thor","Black Widow","Iron-Man","Hawk Eye"]

# features = np.load('Face Recogination/features.npy')
# labels = np.load('Face Recogination/labels.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read('Face Recogination/face_trained.yml')

img = cv2.imread("Face Recogination/src/Validation/jbareham_190421_0890_mcu_ranked_final.0.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("CHARACTER",gray)

#Detect the face in image 

face_rect = haar_cascade.detectMultiScale(gray,1.1,10)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label = {characters[label]} with a confidence of {confidence}')

    cv2.putText(img,str(characters[label]),(x,y-3),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detected Image",img)

cv2.waitKey(0)
