# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 10:53:23 2022

@author: Orkhan Mustafayev
"""

import cv2
from matplotlib import pyplot as pltx

resim = cv2.imread("download.jfif")

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim", resim)

cv2.imshow("resim penceresi", resim)

plt.imshow(resim,cmap="gray")
plt.show()

k = cv2.waitKey(0) & 0xFF

if k == 27:
    print("ESC tusuna basildi")
    
elif k == ord("q"):
    print("q tusuna basildi, resim kayit edildi.")
    cv2.imwrite("download2.jfif", resim)
    
# cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()