import random
import pyglet
import errno
import os
import math
class Mobs(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    compteur = 0

    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, pv, speed, mobName, imageName):
        super().__init__(img, xPixel, yPixel)
        Mobs.compteur += 1
        self.id = Mobs.compteur
        self.x = xBlock
        self.y = yBlock
        self.pv = pv
        self.speed = speed
        self.destinationX = None
        self.destinationY = None
        self.step = 0
        self.mobName = mobName
        self.idPath = None
        self.idZone = -1

    def findDestination(self, path):
        if self.idZone < len(path):
            zone = path[self.idZone]
            self.destinationX = random.randrange(zone.minX, zone.maxX)
            self.destinationY = random.randrange(zone.minY, zone.maxY)
            return True
        return False

    def move(self, level):
        if round(self.x) == round(self.destinationX) and round(self.y) == round(self.destinationY):
            self.idZone += 1
            return self.findDestination(level.findPathById(self))
        distanceRemaning = math.sqrt(pow(self.destinationX - self.x, 2) + pow(self.destinationY - self.y, 2))
        self.x = self.x + self.speed * (self.destinationX - self.x) / distanceRemaning
        self.y = self.y + self.speed * (self.destinationY - self.y) / distanceRemaning
        return True

    def hitByShoot(self, shoot):
        self.pv -= shoot.damage
        shoot.onHitEffect()

