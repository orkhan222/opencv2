# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:35:05 2022

@author: Orkhan Mustafayev
"""

import cv2


cam = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('dronengri.avi', fourrc, 30.0, (640,480))

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("kameradan goruntu alinmadi")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("goruntu sonlandirildi.")
        break
    
cam.release()
out.release()
cv2.destroyAllWindows()
