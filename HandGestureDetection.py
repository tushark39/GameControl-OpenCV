import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self):
        self.mode = False
        self.maxHands = 2
        self.minDetectionConfidence = 0.7
        self.minTrackingConfidence = 0.5

        self.targetHand = mp.solutions.hands
        self.hands = self.targetHand.Hands(self.mode, self.maxHands, self.minDetectionConfidence, self.minTrackingConfidence)

        self.mpLandmarkVisual = mp.solutions.drawing_utils

    def detectLandMark(self, frame):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.processedData = self.hands.process(rgbFrame)

        if self.processedData.multi_hand_landmarks:
            for connections in self.processedData.multi_hand_landmarks:
                self.mpLandmarkVisual.draw_landmarks(frame, connections, self.targetHand.HAND_CONNECTIONS)
        return frame

    def getLandMarks(self, frame):
        landMarkList = []
        if self.processedData.multi_hand_landmarks:
            selectedHand = self.processedData.multi_hand_landmarks[0]
            for index, val in enumerate(selectedHand.landmark):
                frameHeight, frameWidth, framedimension = frame.shape
                Xcord, Ycord = int(val.x * frameWidth), int(val.y * frameHeight)
                landMarkList.append([index, Xcord, Ycord])
        return landMarkList