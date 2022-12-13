import sample.mob.Mobs as m
import random
from copy import deepcopy

class ListMobs:
    def __init__(self):
        self.listMobsOriginels = list()
        self._init_All_Mobs()
        self.listMobsOnMap = list()

    def _init_All_Mobs(self):
        self.listMobsOriginels.append(m.Mobs(0, 0, 100, 20, "Estaca1A", "Estaca1A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 150, 20, "Estaca2A", "Estaca2A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 50, 50, "Estaca3A", "Estaca3A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 250, 30, "Estaca4A", "Estaca4A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 500, 35, "Estaca5A", "Estaca5A.png"))


    def findSpriteByImageName(self, name):
        for sprite in self.listMobsOriginels:
            if sprite.mobName == name:
                return sprite
        return None

    def findSpriteById(self, idSprite):
        for sprite in self.listMobsOriginels:
            if sprite.id == idSprite:
                return sprite
        return None

    def spawnMob(self, zone, id):
        mob = self.findSpriteById(id)
        mob.x = random.randrange(zone.minX, zone.maxX)
        mob.y = random.randrange(zone.minY, zone.maxY)
        self.listMobsOnMap.append(deepcopy(mob))
        print("A mob spawned in x=" + str(mob.x) + " y=" + str(mob.y))
        return None

    def spawnMultipleMobs(self, zone, numberMonsterId1, numberMonsterId2, numberMonsterId3, numberMonsterId4, numberMonsterId5):
        for i in range(numberMonsterId1):
            self.spawnMob(zone, 1)
        for i in range(numberMonsterId2):
            self.spawnMob(zone, 2)
        for i in range(numberMonsterId3):
            self.spawnMob(zone, 3)
        for i in range(numberMonsterId4):
            self.spawnMob(zone, 4)
        for i in range(numberMonsterId5):
            self.spawnMob(zone, 5)

    def order(self):
        templsit = list()
        while len(self.listMobsOnMap) > 0:
            higherMob = self.listMobsOnMap[0]
            for mob in self.listMobsOnMap:
                if (mob.x + mob.y) < (higherMob.x + higherMob.y):
                    higherMob = mob
            templsit.append(higherMob)
            self.listMobsOnMap.remove(higherMob)
        self.listMobsOnMap = templsit
        return self.listMobsOnMap