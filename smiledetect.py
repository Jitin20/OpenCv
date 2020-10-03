import cv2
import time
import numpy as np

smile_cascade=cv2.CascadeClassifier('C:\\Users\\jitin\\PycharmProjects\\facedetect\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml')

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smiles=smile_cascade.detectMultiScale(gray,1.3,3)



    for(x,y,w,h) in smiles:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.imshow('frame', frame)



        k=cv2.waitKey(30) & 0xff
        if k == 27:
            break



cap.release()

cv2.destroyAllWindows()
