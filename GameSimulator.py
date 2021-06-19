import cv2
import HandGestureDetection as hd
# import time
import pyautogui
import math
import FindAxisDistance

# time.sleep(2)

cap = cv2.VideoCapture(0)

handDataCap = hd.HandDetector()
Distance = FindAxisDistance.AxisCal()
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        landMarkList = handDataCap.getLandMarks(frame)
        if len(landMarkList) == 21:
            pyautogui.press('w')
        if len(landMarkList):

            # Left
            lengthL = Distance.findDistance(landMarkList, 4, 8)
            if lengthL < 28:
                pyautogui.press('a')

            # Right
            lengthR = Distance.findDistance(landMarkList, 4,12)
            if lengthR < 28:
                pyautogui.press('d')

            # Down
            lengthD = Distance.findDistance(landMarkList, 4, 16)
            if lengthD < 30:
                pyautogui.press('s')

            # Break
            lengthBreak = Distance.findDistance(landMarkList, 20, 17)
            if lengthBreak < 25:
                break

        cv2.imshow('Simulation', frame)
        if cv2.waitKey(1) == 27:
            break
