import sample.mob.Mobs as m
import random
from copy import deepcopy

class ListMobs:
    def __init__(self):
        self.listMobsOriginels = list()
        self._init_All_Mobs()
        self.listMobsOnMap = list()

    def _init_All_Mobs(self):
        self.listMobsOriginels.append(m.Mobs(0, 0, 100, 1, "Estaca1A", "Estaca1A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 150, 0.2, "Estaca2A", "Estaca2A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 50, 0.5, "Estaca3A", "Estaca3A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 250, 0.3, "Estaca4A", "Estaca4A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 500, 0.35, "Estaca5A", "Estaca5A.png"))


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

    def spawnMob(self, spawningZone,targetZone, id):
        mob = self.findSpriteById(id)
        mob.x = random.randrange(spawningZone.minX, spawningZone.maxX)
        mob.y = random.randrange(spawningZone.minY, spawningZone.maxY)
        mob.destinationX = random.randrange(targetZone.minX, targetZone.maxX)
        mob.destinationY = random.randrange(targetZone.minY, targetZone.maxY)
        self.listMobsOnMap.append(deepcopy(mob))
        print("A mob spawned in x=" + str(mob.x) + " y=" + str(mob.y))
        return None

    def spawnMultipleMobs(self, spawningZone, targetZone, numberMonsterId1, numberMonsterId2, numberMonsterId3, numberMonsterId4, numberMonsterId5):
        for i in range(numberMonsterId1):
            self.spawnMob(spawningZone, targetZone, 1)
        for i in range(numberMonsterId2):
            self.spawnMob(spawningZone, targetZone, 2)
        for i in range(numberMonsterId3):
            self.spawnMob(spawningZone, targetZone, 3)
        for i in range(numberMonsterId4):
            self.spawnMob(spawningZone, targetZone, 4)
        for i in range(numberMonsterId5):
            self.spawnMob(spawningZone, targetZone, 5)

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

    def moveMobs(self, zone):
        for mob in self.listMobsOnMap:
            mob.move(zone)
