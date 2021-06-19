import cv2
import HandGestureDetection as hd
import time
import pyautogui
import math

time.sleep(2)

cap = cv2.VideoCapture(0)

handDataCap = hd.HandDetector()

while True:
    success, img = cap.read()
    if success:
        img = cv2.flip(img, 1)
        landMarkList = handDataCap.getLandMarks(img)
        if len(landMarkList)==21:
            pyautogui.press('w')


        if len(landMarkList):

            #Left
            Lx1, Ly1 = landMarkList[4][1], landMarkList[4][2]
            Lx2, Ly2 = landMarkList[8][1], landMarkList[8][2]
            lengthL = math.hypot(Lx2 - Lx1, Ly2 - Ly1)
            if lengthL<28:
                pyautogui.press('a')


            # Right
            Rx1, Ry1 = landMarkList[4][1], landMarkList[4][2]
            Rx2, Ry2 = landMarkList[12][1], landMarkList[12][2]
            lengthL = math.hypot(Rx2 - Rx1, Ry2 - Ry1)
            if lengthL < 28:
                pyautogui.press('d')

            # Down
            Dx1, Dy1 = landMarkList[4][1], landMarkList[4][2]
            Dx2, Dy2 = landMarkList[16][1], landMarkList[16][2]
            lengthD = math.hypot(Dx2 - Dx1, Dy2 - Dy1)
            # print(lengthD)
            if lengthD < 30:
                pyautogui.press('s')

            # Break
            Breakx1, Breaky1 = landMarkList[20][1], landMarkList[20][2]
            Breakx2, Breaky2 = landMarkList[17][1], landMarkList[17][2]
            lengthBreak = math.hypot(Breakx2 - Breakx1, Breaky2 - Breaky1)
            if lengthBreak < 25:
                break

        cv2.imshow('Image', img)
        if cv2.waitKey(1) == 27:
            break