import sample.Mobs as m
import random

class ListMobs:
    def __init__(self):
        self.listMobsOriginels = list()
        self._init_All_Mobs()
        self.listMobsOnMap = list()

    def _init_All_Mobs(self):
        self.listMobsOriginels.append(m.Mobs(0, 0, 100, 20, "Estaca1A"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 150, 20, "Estaca2A"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 50, 50, "Estaca3A"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 250, 30, "Estaca4A"))
        self.listMobsOriginels.append(m.Mobs(0, 0, 500, 35, "Estaca5A"))


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
        mob.x = random.randint(zone.minX, zone.maxX)
        mob.y = random.randint(zone.minY, zone.maxY)
        self.listMobsOnMap.append(mob)
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
