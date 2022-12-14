import sample.Zone as zone
import random

class Level:

    def __init__(self):
        self.spawningZone = zone.Zone(0, 0, 5, 5)
        self.path1 = list()
        self._init_path(self.path1)
        self.path2 = list()
        self._init_path(self.path2)
        self.path3 = list()
        self._init_path(self.path3)

    def _init_path(self, path):
        for i in range(5):
            x = random.randint(0, 45)
            y = random.randint(0, 45)
            path.append(zone.Zone(x, y, x+5, y+5))