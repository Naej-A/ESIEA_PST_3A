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
            x = random.randint(0, 70)
            y = random.randint(0, 70)
            path.append(zone.Zone(x, y, x+5, y+5))

    def findPathById(self, mob):
        if mob.idPath == 1:
            return self.path1
        if mob.idPath == 2:
            return self.path2
        if mob.idPath == 3:
            return self.path3
        return None
