import cv2
import HandGestureDetection as hd
# import time
import pydirectinput as pyautogui
#import pyautogui
import math
import FindAxisDistance
import pygame

from directkeys import PressKey, W, A, S, D,ReleaseKey
# time.sleep(2)
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(1)

handDataCap = hd.HandDetector()
Distance = FindAxisDistance.AxisCal()
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        landMarkList = handDataCap.getLandMarks(frame)
        #if len(landMarkList) == 21:
            #pyautogui.press('w')
        if len(landMarkList):

            # Left
            lengthL = Distance.findDistance(landMarkList, 4, 8)
            if lengthL < 28:
                PressKey(A)
            elif lengthL >28:
                ReleaseKey(A)
            
            # Right
            lengthR = Distance.findDistance(landMarkList, 4,12)
            if lengthR < 28:
                PressKey(D)
            elif lengthL >28:
                ReleaseKey(D)

#             # Down
#             lengthD = Distance.findDistance(landMarkList, 4, 16)
#             if lengthD < 30:
#                 pyautogui.press('down')
#                 # pygame.KEYDOWN

#             # Break
            lengthBreak = Distance.findDistance(landMarkList, 12, 0)
            if lengthBreak < 100:
                PressKey(W)
            elif lengthL >100:
                ReleaseKey(W)
# #break

        cv2.imshow('Simulation', frame)
        if cv2.waitKey(1) == 27:
            break
