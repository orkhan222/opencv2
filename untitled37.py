# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:35:05 2022

@author: Orkhan Mustafayev
"""

import cv2


cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("kamera tanimadi")
    exit()

while True:
    ret, frame = cam.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("kameradan goruntu okunamiyor")
        break
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("goruntu sonlandirildi.")
        break
    
cam.release()
cv2.destroyAllWindows()