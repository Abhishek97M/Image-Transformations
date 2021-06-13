import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
im=cv2.imread("images.jpg")
(h, w) = im.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))
M[0, 2] += (nW / 2) - cX
M[1, 2] += (nH / 2) - cY
rotmin=cv2.warpAffine(im, M, (nW, nH))
#plt.imshow(rotmin)
cv2.imwrite("problem-3.jpg",rotmin)

