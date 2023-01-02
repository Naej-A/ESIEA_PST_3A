import sample.mob.Mobs as m
import random
from copy import deepcopy

class ListMobs:
    def __init__(self):
        self.listMobsOriginels = list()
        self._init_All_Mobs()
        self.listMobsOnMap = list()

    def _init_All_Mobs(self):
        self.listMobsOriginels.append(m.Mobs(0, 0, 100, 1, "Estaca1A", "Tux.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 150, 0.2, "Estaca2A", "Estaca2A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 50, 0.5, "Estaca3A", "Estaca3A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 250, 0.3, "Estaca4A", "Estaca4A.png"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 500, 0.35, "Estaca5A", "Estaca5A.png"))


    def findSpriteByeName(self, name):
        for sprite in self.listMobsOriginels:
            if sprite.mobName == name:
                return sprite
        return None

    def findSpriteById(self, idSprite):
        for sprite in self.listMobsOriginels:
            if sprite.id == idSprite:
                return sprite
        return None

    def spawnMob(self, spawningZone, name):
        mob = self.findSpriteByeName(name)
        mob.idPath = random.randint(1, 3)
        mob.x = random.randrange(spawningZone.minX, spawningZone.maxX)
        mob.y = random.randrange(spawningZone.minY, spawningZone.maxY)
        mob.destinationX = mob.x
        mob.destinationY = mob.y
        self.listMobsOnMap.append(deepcopy(mob))
        print("A mob spawned in x=" + str(mob.x) + " y=" + str(mob.y))
        return None

    def spawnMultipleMobs(self, level, mobDictionary):
        spawningZone = level.spawningZone
        for mobToSpawn in mobDictionary.keys():
            for numberOfMobsToSpawn in range(mobDictionary.get(mobToSpawn)):
                self.spawnMob(spawningZone, mobToSpawn)

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

    def moveMobs(self, level):
        for mob in self.listMobsOnMap:
            if not mob.move(level): #Si le mob n'a pas bougé (donce si il est au bout)
                self.listMobsOnMap.remove(mob)

    def removeDeadmobs(self):
        mobNumber = 0
        while mobNumber < len(self.listMobsOnMap):
            mob = self.listMobsOnMap[mobNumber]
            if mob.pv <= 0:
                self.listMobsOnMap.remove(mob)
            else:
                mobNumber += 1

