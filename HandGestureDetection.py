import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self):
        # Initializers
        self.targetHand = mp.solutions.hands
        self.hands = self.targetHand.Hands(min_detection_confidence=0.7)
        self.mpLandmarkVisual = mp.solutions.drawing_utils

    def getLandMarks(self, frame,landLoc=True,LandLocPoint=False):
        landMarkList = []
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.processedData = self.hands.process(rgbFrame)
        if self.processedData.multi_hand_landmarks:
            selectedHand = self.processedData.multi_hand_landmarks[0]
            for index, val in enumerate(selectedHand.landmark):
                frameHeight, frameWidth, framedimension = frame.shape
                Xcord, Ycord = int(val.x * frameWidth), int(val.y * frameHeight)
                landMarkList.append([index, Xcord, Ycord])
                if LandLocPoint:
                    cv2.circle(frame, (Xcord, Ycord), 10, (255, 0, 0), cv2.FILLED)
                if landLoc:
                    self.mpLandmarkVisual.draw_landmarks(frame, selectedHand, self.targetHand.HAND_CONNECTIONS)

        return landMarkList
