#face and smile detection
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)  #'0' denotes webcam of your pc
cap.set(3,640)  #'3' denotes length
cap.set(4,480)  #'4' denotes breadth

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.putText(img, 'face', (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 1, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w] #roi=region of interest inside the rectangle of the face detect in the gray img
        roi_color = img[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray,1.7,26)
        for (ex,ey,ew,eh) in smile: 
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
            cv2.putText(roi_color, 'smile', (ex, ey-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 1, cv2.LINE_AA)
    
    cv2.imshow('img',img)
    #cv2.imshow('gray',gray)   #displays image in gray scale
    cv2.waitKey(1)
    
cap.release()  #closes the webcam
cv2.destroyAllWindows()   #closes the windows
