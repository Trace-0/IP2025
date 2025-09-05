import numpy as np
import cv2
# Create a black image
# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("dog.jpg")
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(960,638),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img,(447,63), 63, (0,0,255), 10)
img = cv2.ellipse(img,(256,256),(100,50),0,0,90,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 2,(255,255,255),12,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()