# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:24:46 2022

@author: Orkhan Mustafayev
"""

import cv2

import numpy as np

sifir =np.zeros([300,300])

bir = np.ones([300,300])


cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

cv2.imshow("sifir",sifir)
cv2.imshow("bir", bir)

cv2.waitKey(0)

cv2.destroyAllWindows()