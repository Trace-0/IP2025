import cv2
import numpy as np

ix = -1
iy = -1
drawing = False
font = cv2.FONT_HERSHEY_SIMPLEX

def nothing(x):
    pass

def draw_box(event,x,y,flags,param):
    global ix,iy, drawing, img, draw_layer

    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        drawing = True
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = draw_layer.copy()
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
            cv2.putText(img, f'Mouse Position: ({ix}, {iy}) - ({x}, {y}) / {draw_layer[y, x]}', (10, 20), font,0.5, (255,255,255),1, cv2.LINE_AA)
        else:
            img = draw_layer.copy()
            cv2.putText(img, f'Mouse Position: ({x}, {y}) / {draw_layer[y, x]}', (10, 20), font, 0.5, (255,255,255),1, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        draw_layer[iy:y, ix:x, 2] = 255
        drawing = False
        img = draw_layer.copy()

img = cv2.imread('mountain.jpg')
draw_layer = img.copy()
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.setMouseCallback('image',draw_box)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()