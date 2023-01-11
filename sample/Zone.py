import random
class Zone:
    def __init__(self, minX, minY, maxX, maxY):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY

    def getPosition(self):
        X = random.uniform(self.minX, self.maxX)
        Y = random.uniform(self.minY, self.maxY)
        return X, Y
