import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
#from picamera.array import PiRGBArray
#from picamera import PiCamera
cap = cv2.VideoCapture(0)
while True:
  ret,frame = cap.read()
  image = frame.array
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF

  if key == ord("s"):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grey scale
        gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
        edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
        screenCnt = None
        for c in cnts:
          peri = cv2.arcLength(c, True)
          approx = cv2.approxPolyDP(c, 0.018 * peri, True)
          if len(approx) == 4:
            screenCnt = approx
            break
        if screenCnt is None:
          detected = 0
          print ("No contour detected")
        else:
          detected = 1
        if detected == 1:
          cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(image,image,mask=mask)
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]
        text = pytesseract.image_to_string(Cropped, config='--psm 11')
        print("Detected Number is:",text)

        cv2.imshow("Frame", image)
        cv2.imshow('Cropped',Cropped)
        cv2.waitKey(0)
        break
cv2.destroyAllWindows()
