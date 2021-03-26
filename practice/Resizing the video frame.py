import cv2 as cv 
# Importing Video File
capture = cv.VideoCapture("src/Screen Recording 2021-03-16 at 9.43.43 PM.mov")

# Function to rescale Frame

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)


#function to run the each frame of the video

while True:

    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame,0.3)

    # cv.imshow('Video',frame)
    cv.imshow('Video',frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

capture.release()

cv.destroyAllWindows()
