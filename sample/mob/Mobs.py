import random
import pyglet
import errno
import os
import math
import sample.IsometricTools as IsometricTools
class Mobs(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    compteur = 0

    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, pv, speed, mobName, scale):
        super().__init__(img, xPixel, yPixel)
        Mobs.compteur += 1
        self.id = Mobs.compteur
        self.xBlock = xBlock
        self.yBlock = yBlock
        self.pv = pv
        self.speed = speed
        self.destinationX = None
        self.destinationY = None
        self.step = 0
        self.mobName = mobName
        self.idPath = None
        self.idZone = -1
        self.slowTokens = list()
        self.scale_x = 1

    def findDestination(self, path):
        if self.idZone < len(path):
            zone = path[self.idZone]
            self.destinationX = random.randrange(zone.minX, zone.maxX)
            self.destinationY = random.randrange(zone.minY, zone.maxY)
            return True
        return False

    def orientSprite(self):
        if self.destinationY - self.destinationX < self.yBlock - self.xBlock:
            self.scale_x = 1
        else:
            self.scale_x = -1

    def move(self, level):
        self.orientSprite()
        slowFactor = self.getSlowFactor()
        speed = 0.12 * self.speed * (1 - slowFactor)
        distanceRemaning = math.sqrt(pow(self.destinationX - self.xBlock, 2) + pow(self.destinationY - self.yBlock, 2))
        if distanceRemaning < self.speed:
            self.idZone += 1
            return self.findDestination(level.findPathById(self))
        self.xBlock = self.xBlock + speed * (self.destinationX - self.xBlock) / distanceRemaning
        self.yBlock = self.yBlock + speed * (self.destinationY - self.yBlock) / distanceRemaning
        return True

    def getSlowFactor(self):
        if len(self.slowTokens) > 0:
            slowFactor = round((max(self.slowTokens) + 5) / 10) + 1
        else:
            slowFactor = 0
        return slowFactor

    def hitByShoot(self, shoot):
        self.pv -= shoot.damage
        shoot.onHitEffect()

    def updatePixelCoordinates(self, gameProgress):
        self.x, self.y = IsometricTools.coordinateToPixel(gameProgress, self.xBlock, self.yBlock)
        # Décalage du sprite lié à sa taille

    def onDeathEffect(self, gameProgress):
        return None