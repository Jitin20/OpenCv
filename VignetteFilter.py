import numpy as np
import cv2
#reading the image
#img= cv2.imread('jitu.jpg')
cap=cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    frame= cv2.resize(frame,(640,640))

#Extracting Height and width from the image

    rows,cols= frame.shape[:2]

#Generating Mask

    X_resultant_kernel = cv2.getGaussianKernel(cols,200)
    Y_resultant_kernel = cv2.getGaussianKernel(rows,200)

    resultant = X_resultant_kernel * Y_resultant_kernel.T

#Creating mask and normalizing

    mask = 255 * resultant / np.linalg.norm(resultant)
    output = np.copy(frame)

# applying the mask to each channel in the input image
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask

# displaying the orignal image
    cv2.imshow('Original', frame)

# displaying the vignette filter image
    cv2.imshow('VIGNETTE', output)

# Maintain output window utill
# user presses a key
    cv2.waitKey(1)
cap.release()
# Destroying present windows on screen
cv2.destroyAllWindows()
