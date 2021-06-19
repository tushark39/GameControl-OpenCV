import math
class AxisCal():
    def findDistance(self,landMarkList,landMarkPoint1,landMarkPoint2):
        xCord1, yCord1 = landMarkList[landMarkPoint1][1], landMarkList[landMarkPoint1][2]
        xCord2, yCord2 = landMarkList[landMarkPoint2][1], landMarkList[landMarkPoint2][2]
        distance = math.hypot(xCord2 - xCord1, yCord2 - yCord1)

        return distance