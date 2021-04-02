import os
import cv2 
import numpy as np 


haar_cascade = cv2.CascadeClassifier("Face Recogination/haar_face.xml")

characters = ["Loki","Thor","Black Widow","Iron-Man","Hawk Eye"]

DIR = r'Face Recogination/src/Train'

features = []
labels = []

def create_train():
    for character in characters:
        path = os.path.join(DIR,character)
        label = characters.index(character)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv2.imread(img_path)

            # gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(img_array,1.1,4)

            for (x,y,w,h) in faces_rect:
                faces_roi = img_array[y:y+h,x:x+w]
                faces_roi = cv2.cvtColor(faces_roi,cv2.COLOR_BGR2GRAY)
                features.append(faces_roi)
                labels.append(label)

create_train()

print("Training competed.....")

features = np.array(features,dtype='object')
labels = np.array(labels)

# print(f'length of the feature: {len(features)}')
# print(f'length of the label: {len(labels)}')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Train the recogniger on feature and label

face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels) 