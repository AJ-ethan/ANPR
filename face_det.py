import cv2
import time

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#writer = cv2.VideoWriter('../DATA/student_capture.mp4', cv2.VideoWriter_fourcc(*'XVID'),25, (width, height))
fps = 5
i = 0
j= 0
tracker = cv2.TrackerCSRT_create()
ret, frame = cap.read()

#bbox = cv2.selectROI(frame)
#print("____________________",bbox)
#ok = tracker.init(frame,bbox)
temp = 0
face_cascde = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while True:
    ret, frame = cap.read()
    
    time.sleep(1/fps)
 
    face_rects = face_cascde.detectMultiScale(frame,scaleFactor=1.3, minNeighbors=3)
    if temp:
	    #ok = tracker.init(frame,face_rects)
	    ok,bbox=tracker.update(frame)
	    if ok:
	    	(x,y,w,h)=[int(v) for v in bbox]
	    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
	    else:
	    	cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2) 
    
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 4)
        ok = tracker.init(frame,(x,y,w,h))
        cv2.imwrite('img.png', frame[y:y+h,x:x+w])
        #writer.write(frame)
        temp = 1
        j = j+1
        
    cv2.imshow('frame',frame)
    i =i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
writer.release()
cv2.destroyAllWindows()
