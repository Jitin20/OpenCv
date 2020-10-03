#importing open cv library
import cv2
#importing date and time library
import datetime
#Usage of haarcascades (Cascades are precontained with some set of input data)
face_cascade= cv2.CascadeClassifier('C:\\Users\\jitin\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
#Capturing the video from Webcam
cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    #setting date and time variable
    datet=str(datetime.datetime.now())
    #setting the font
    font=cv2.FONT_ITALIC
    #For getting text on the frame screen
    frame=cv2.putText(frame,datet,(100,100),font,1,(0,0,255),2)
    #As face recon only works on grayscale so conversion is necessory
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Identifying the face
    faces=face_cascade.detectMultiScale(gray,1.3,4)
#setting up the circle in the face
    for(x,y,w,h) in faces:
        cv2.circle(frame,(x+w//2,y+h//2),w//2,(255,0,0),3)
        #Display command
        cv2.imshow('frame',frame)
        
        k=cv2.waitKey(30) & 0xff
        if k == 27:
            break
#releasing all the frames
cap.release()

