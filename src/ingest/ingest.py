import cv2
import os

videoFeed = cv2.VideoCapture("C:/Users/Wesley Whittle/Documents/GitHub/Dynamic-AI-AR/src/ingest/data/testData.mp4")

try:
    if not os.path.exists('output'):
        os.makedirs('output')

except OSError:
    print ("Error creating the directory")

currentFrame = 0

while(True):
    ret,frame = videoFeed.read()

    if ret:
        name = "./output/frame" + str(currentFrame) + ".jpg"
        print ("Creating..." + name)

        cv2.imwrite(name, frame)

        currentFrame += 1
    else:
        break

videoFeed.release()
cv2.destroyAllWindows()