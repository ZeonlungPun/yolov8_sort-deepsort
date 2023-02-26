import numpy as np
from ultralytics import YOLO
import cv2,cvzone,math


cap=cv2.VideoCapture("E:\\opencv\\yolo8Sort\\Videos\\ppe-1.mp4")
model=YOLO("../weights/bestppe.pt")

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']



while True:
    success,img=cap.read()
    results=model(img,stream=True)


    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)
            w,h=x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h),l=9)

            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            currentClass=classNames[cls]
            cvzone.putTextRect(img,f'{classNames[cls]}',(max(0,x1),max(35,y1)),
                               scale=1,offset=3,thickness=1)





    cv2.imshow("image",img)
    cv2.waitKey(1)
