import cv2
import numpy as np
#cam
cap = cv2.VideoCapture(0)
#face
face_xml = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#video
while (1):
    _,frame = cap.read()
    faces = face_xml.detectMultiScale(frame , 1.2 , 4) 

    for (x , y , w , h) in faces:
        roi = frame[y:y+h , x:x+w]
        blur = cv2.GaussianBlur(roi  , (91,91) , 0)

        frame[y:y+h , x:x+w] = blur
    if faces==():
        cv2.putText(frame , 'no face detect!' , (20 , 50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,0,255))
    cv2.imshow('blur face' , frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()