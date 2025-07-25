import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
model=YOLO('best.pt')
cap=cv2.VideoCapture('p.mp4')
count=0
w=1020
h=500
while True:
    ret,frame=cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
        break
    frame=cv2.resize(frame,(1020,500))
    results=model(frame)
    aframe=results[0].plot()



        


    


        


    cv2.imshow('FRAME',aframe)
    if cv2.waitKey(0)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()