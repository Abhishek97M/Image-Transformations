import numpy as np
import cv2
from matplotlib import pyplot as plt
from utils import ymin,xmin,xmax,ymax,yminxmax,xminymax,xminymin,xmaxymax,pixlev
im=cv2.imread("images.jpg")
(h, w) = im.shape[:2] 
centerx =w//2
centery =h//2
r,g,b=im[centerx,centery]
r,g,b=pixlev(r,g,b,50)
im[centerx,centery]=[r,g,b]
per=50
im=ymin(im,centerx,centery,per)
im=xmin(im,centerx,centery,per)
im=xmax(im,centerx,centery,per)
im=ymax(im,centerx,centery,per)
im=yminxmax(im,centerx,centery,per)
im=xminymax(im,centerx,centery,per)
im=xminymin(im,centerx,centery,per)
im=xmaxymax(im,centerx,centery,per)
#cv2.imwrite("problem-5.jpg",im)
plt.imshow(im)
plt.show()
