import sample.Zone as zone
import random

class Level:

    def __init__(self):
        self.spawningZone = zone.Zone(-18, 22, -23, 28)
        self.path1 = list()
        self._init_path1(self.path1)
        self.path2 = list()
        self._init_path2(self.path2)
        self.path3 = list()
        self._init_path3(self.path3)

    def _init_path1(self, path):
            path.append(zone.Zone(-11, 30, -17, 36))
            path.append(zone.Zone(-11, 38, -17, 44))
            path.append(zone.Zone(-5, 39, -7, 42))#commun tout le monde
            path.append(zone.Zone(20, 97, 23, 100))
            path.append(zone.Zone(34, 97, 34, 97))
            path.append(zone.Zone(30, 93, 38, 101))#commun
            path.append(zone.Zone(15, 60, 25, 70))
            path.append(zone.Zone(101, 53, 103, 55))

    def _init_path2(self, path):
            path.append(zone.Zone(-11, 30, -17, 36))
            path.append(zone.Zone(-11, 38, -17, 44))
            path.append(zone.Zone(-5, 39, -7, 42))#commun tout le monde
            path.append(zone.Zone(20, 97, 23, 100))
            path.append(zone.Zone(34, 97, 34, 97))
            path.append(zone.Zone(30, 93, 38, 101))#commun
            path.append(zone.Zone(40, 120, 40, 120))
            path.append(zone.Zone(101, 53, 103, 55))

    def _init_path3(self, path):
            path.append(zone.Zone(-11, 30, -17, 36))
            path.append(zone.Zone(-11, 38, -17, 44))
            path.append(zone.Zone(-5, 39, -7, 42))#commun tout le monde
            path.append(zone.Zone(0, 50, 3, 52))
            path.append(zone.Zone(95, 30, 98, 33))
            path.append(zone.Zone(95, 60, 98, 60))

            path.append(zone.Zone(101, 53, 103, 55))


    def findPathById(self, mob):
        if mob.idPath == 1:
            return self.path1
        if mob.idPath == 2:
            return self.path2
        if mob.idPath == 3:
            return self.path3
        return None
