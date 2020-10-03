import cv2
img=cv2.imread('jitu.jpg',1)

img=cv2.circle(img,(50,50),200,(255,0,0),4)

img=cv2.arrowedLine(img,(0,0),(255,255),(255,0,0),5 )

#similarly we can add rectangle,square and even texts in the frame.
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


