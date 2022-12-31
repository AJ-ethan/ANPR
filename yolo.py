from pydarknet import Detector, Image
import cv2
import numpy as np
import imutils
from imutils.video import FPS
from imutils.video import VideoStream


#Files used in the program. Make changes for input, config, weights etc
INPUT_FILE=0
OUTPUT_FILE='output.avi'
LABELS_FILE='data/coco.names'
CONFIG_FILE='cfg/yolov3.cfg'
WEIGHTS_FILE='yolov3.weights'
DATA_FILE="cfg/coco.data"
CONFIDENCE_THRESHOLD=0.3


#FPS calculator enables
fps = FPS().start()

#Declaration of output file to save the analysed video
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, 30,
	(800, 600), True)

#Read all labels
LABELS = open(LABELS_FILE).read().strip().split("\n")
np.random.seed(4)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")
#Create a dictionary with different colors for each class of labels
COLOR_LABEL={}
for i in range(0, len(LABELS)):
    COLOR_LABEL[LABELS[i]]=COLORS[i]

#Read the YOLO files
net = Detector(bytes(CONFIG_FILE, encoding="utf-8"), bytes(WEIGHTS_FILE, encoding="utf-8"), 0, bytes(DATA_FILE,encoding="utf-8"))

#Setting the video reader
vs = cv2.VideoCapture(INPUT_FILE)
cnt=0


#We have set a limit of 500 frames. This can be changed
while True and cnt < 500:
    cnt+=1
    print ("Frame number", cnt)
    try:
        (grabbed, image) = vs.read()
    except:
        break

    img_darknet = Image(image)
    
    #Run detection on each frame

    results = net.detect(img_darknet)
    
    #make bounding boxes and text for each image
    for cat, score, bounds in results:

        x, y, w, h = bounds
        color = [int(c) for c in COLOR_LABEL[str(cat.decode("utf-8"))]]
        text = "{}: {:.4f}".format(str(cat.decode("utf-8")), score)
        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), color, thickness=2)
        
        cv2.putText(img,text,(int(x - w/2),int(y -h/2 -5)),cv2.FONT_HERSHEY_COMPLEX,1,color)


    #write frame to output file
    writer.write(cv2.resize(image,(800, 600)))
    fps.update()
    
fps.stop()

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()

# release the file pointers
print("[INFO] cleaning up...")
writer.release()
vs.release()from pydarknet import Detector, Image
import cv2
import numpy as np
import imutils
from imutils.video import FPS
from imutils.video import VideoStream


#Files used in the program. Make changes for input, config, weights etc
INPUT_FILE='traffic_1.mp4'
OUTPUT_FILE='output.avi'
LABELS_FILE='data/coco.names'
CONFIG_FILE='cfg/yolov3.cfg'
WEIGHTS_FILE='yolov3.weights'
DATA_FILE="cfg/coco.data"
CONFIDENCE_THRESHOLD=0.3


#FPS calculator enables
fps = FPS().start()

#Declaration of output file to save the analysed video
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, 30,
	(800, 600), True)

#Read all labels
LABELS = open(LABELS_FILE).read().strip().split("\n")
np.random.seed(4)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")
#Create a dictionary with different colors for each class of labels
COLOR_LABEL={}
for i in range(0, len(LABELS)):
    COLOR_LABEL[LABELS[i]]=COLORS[i]

#Read the YOLO files
net = Detector(bytes(CONFIG_FILE, encoding="utf-8"), bytes(WEIGHTS_FILE, encoding="utf-8"), 0, bytes(DATA_FILE,encoding="utf-8"))

#Setting the video reader
vs = cv2.VideoCapture(INPUT_FILE)
cnt=0


#We have set a limit of 500 frames. This can be changed
while True and cnt < 500:
    cnt+=1
    print ("Frame number", cnt)
    try:
        (grabbed, image) = vs.read()
    except:
        break

    img_darknet = Image(image)
    
    #Run detection on each frame

    results = net.detect(img_darknet)
    
    #make bounding boxes and text for each image
    for cat, score, bounds in results:

        x, y, w, h = bounds
        color = [int(c) for c in COLOR_LABEL[str(cat.decode("utf-8"))]]
        text = "{}: {:.4f}".format(str(cat.decode("utf-8")), score)
        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), color, thickness=2)
        
        cv2.putText(img,text,(int(x - w/2),int(y -h/2 -5)),cv2.FONT_HERSHEY_COMPLEX,1,color)


    #write frame to output file
    writer.write(cv2.resize(image,(800, 600)))
    fps.update()
    
fps.stop()

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()

# release the file pointers
print("[INFO] cleaning up...")
writer.release()
vs.release()


