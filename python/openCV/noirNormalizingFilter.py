### Attempts to normalize the color spectrum of an image received from a NoIR camera

## imports
import cv2

## variable init
TYPE = "FLE" # "CAM" for camera, "FLE" for file
FILE = r"C:\droneshit\noir.png"
FLTR = True # filter on or off

## functions
def drawFilter(frame):

    return frame

##--------------- Main ---------------##

if(TYPE == "CAM"):
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        # DRAW HUD -- SHOULD BE FINAL STEP!
        frame = drawFilter(frame)
        frame = cv2.resize(frame, (1280, 720)) # resize to an actual good dimension

        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if(TYPE == "FLE"):
    frame = cv2.imread(FILE)
    if(FLTR == True):
        frame = drawFilter(frame)
    cv2.imshow('Camera Feed', frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
