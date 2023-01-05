import os

import pyglet

import sample.mob.Mobs as m
import random

class ListMobs:
    def __init__(self):
        # self.listMobsOriginels = list()
        # self._init_All_Mobs()
        self.listMobsOnMap = list()

    # def _init_All_Mobs(self):
    #     pathToImage = os.getcwd() +"/ressources/" + "Student.png"
    #     binary_file_image =  open(pathToImage, 'rb')  # Lecture du fichier en binaire
    #     image = pyglet.image.load(pathToImage, file=binary_file_image)
    #     self.listMobsOriginels.append(m.Mobs(image, 0, 0, 0, 0, 100, 1, "Student"))
    #     self.listMobsOriginels.append(m.Mobs(image, 0, 0, 0, 0, 150, 0.2, "Energic"))
    #     self.listMobsOriginels.append(m.Mobs(image, 0, 0, 0, 0, 50, 0.5, "Engineer"))
    #     self.listMobsOriginels.append(m.Mobs(image, 0, 0, 0, 0, 250, 0.3, "GoMuscu"))
    #     self.listMobsOriginels.append(m.Mobs(image, 0, 0, 0, 0, 500, 0.35, "Vehicule"))


    # def findSpriteByeName(self, name):
    #     for sprite in self.listMobsOriginels:
    #         if sprite.mobName == name:
    #             return sprite
    #     return None

    # def findSpriteById(self, idSprite):
    #     for sprite in self.listMobsOriginels:
    #         if sprite.id == idSprite:
    #             return sprite
    #     return None

    def spawnMob(self, spawningZone, name):
        directory = "ressources/" + name #+ name
        files = os.listdir(directory)
        # random_file = random.choice(files)
        frameList = list()
        for image in files:
            pathToImage = os.path.join(directory, image)
            binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
            sprit = pyglet.image.load(pathToImage, file=binary_file_image)
            frameList.append(sprit)
        if name == "Student":
            HP = 100
            SPEED = 0.1
        elif name == "Energic":
            HP = 100
            SPEED = 0.15
        elif name == "Vehicule":
            HP = 2000
            SPEED = 0.03
        elif name == "GoMuscu":
            HP = 500
            SPEED = 0.12
        elif name == "Engineer":
            HP = 1
            SPEED = 0.08
        else:
            return None
        image = pyglet.image.Animation.from_image_sequence(frameList, 0.05/SPEED)
        mob = m.Mobs(image, 0, 0, 0, 0, HP, SPEED, name)

        mob.idPath = random.randint(1, 3)
        mob.xBlock = random.randrange(spawningZone.minX, spawningZone.maxX)
        mob.yBlock = random.randrange(spawningZone.minY, spawningZone.maxY)
        mob.destinationX = mob.xBlock
        mob.destinationY = mob.yBlock
        self.listMobsOnMap.append(mob)
        print("A mob spawned in x=" + str(mob.xBlock) + " y=" + str(mob.yBlock))
        return None

    def spawnMultipleMobs(self, level, mobDictionary):
        spawningZone = level.spawningZone
        for mobToSpawn in mobDictionary.keys():
            for numberOfMobsToSpawn in range(mobDictionary.get(mobToSpawn)):
                self.spawnMob(spawningZone, mobToSpawn)
        return

    def order(self):
        templsit = list()
        while len(self.listMobsOnMap) > 0:
            higherMob = self.listMobsOnMap[0]
            for mob in self.listMobsOnMap:
                if (mob.xBlock + mob.yBlock) < (higherMob.xBlock + higherMob.yBlock):
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

