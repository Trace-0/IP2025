import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dsu1.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[317,282],[759,312],[323,532],[765,506]])
pts2 = np.float32([[0,0],[600,0],[0,260],[600,260]])
M = cv2.getPerspectiveTransform(pts1,pts2)
print(M)
dst = cv2.warpPerspective(img,M,(600,260))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()