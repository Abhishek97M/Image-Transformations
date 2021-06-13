import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
im=cv2.imread("images.jpg")
rows,cols,r=im.shape
(h, w) = im.shape[:2]
(cX, cY) = (w // 2, h // 2)
con=cols*25/100
Mx = np.float32([[1,0,con],[0,1,0]])
cos = np.abs(Mx[0, 0])
sin = np.abs(Mx[0, 1])
nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))
Mx[0, 2] += (nW / 2) - cX
Mx[1, 2] += (nH / 2) - cY
dstx = cv2.warpAffine(im,Mx,(int(cols+con),rows))
#cv2.imwrite("problem-1.jpg",dstx)
plt.imshow(dstx)
plt.show()
