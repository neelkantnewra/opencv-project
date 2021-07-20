import cv2 
import mediapipe as mp 
import time

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 

hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

ptime = 0 
ctime = 0


while True:
    success,img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id==8 or id==4:
                    cv2.circle(img,(cx,cy),15,(0,25,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    # print(result.multi_hand_landmarks)


    cv2.imshow("Image",img)
    cv2.waitKey(1)
