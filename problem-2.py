import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
im=cv2.imread("images.jpg")
rows,cols,r=im.shape
(h, w) = im.shape[:2]
(cX, cY) = (w // 2, h // 2)
con=rows*25/100
My = np.float32([[1,0,0],[0,1,con]])
cos = np.abs(My[0, 0])
sin = np.abs(My[0, 1])
nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))
My[0, 2] += (nW / 2) - cX
My[1, 2] += (nH / 2) - cY
dsty = cv2.warpAffine(im,My,(cols,int(rows+con)))
#cv2.imwrite("problem-2.jpg",dsty)
plt.imshow(dsty)
plt.show()

