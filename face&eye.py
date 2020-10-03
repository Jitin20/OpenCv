import cv2
import datetime
face_cascade= cv2.CascadeClassifier('C:\\Users\\jitin\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
#Add the cascade file for eye
eye_cascade= cv2.CascadeClassifier('C:\\Users\\jitin\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    datet=str(datetime.datetime.now())
    font=cv2.FONT_ITALIC
    frame=cv2.putText(frame,datet,(100,100),font,1,(0,0,255),2)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,4)
    #detecting eyes
    eyes=eye_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.circle(frame,(x+w//2,y+h//2),w//2,(255,0,0),3)
        #showing rectangle for eyes
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
        cv2.imshow('frame',frame)


        k=cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()

