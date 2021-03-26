import cv2 as cv 

capture = cv.VideoCapture("src/Screen Recording 2021-03-16 at 9.43.43 PM.mov")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

capture.release()

cv.destroyAllWindows()
