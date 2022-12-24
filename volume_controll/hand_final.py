import cv2
import mediapipe as mp
import numpy as np
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
while True:
    success,img=cap.read()
    imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)


    cv2.imshow("Image",img)
    cv2.waitKey(1)