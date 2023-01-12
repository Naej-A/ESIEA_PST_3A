from sample.mob.Mobs import Mobs
import math
import sample.Zone as Zone

class MobsSpawners(Mobs):

    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, pv, speed, tear, mobName, scale):
        super().__init__(img, xPixel, yPixel, xBlock, yBlock, pv, speed, tear, mobName, scale)
        if mobName == "Engineer":
            self.spawnedMobName = "Bulldozer"
            self.castCooldown = 5 * 60 #Fait spawn un bulldozer toutes les 3 secondes
            self.spawnRange = 2
        self.castCooldownCounter = 0 #Permet de compter 3 secondes

    def move(self, level):
        self.castCooldownCounter += 1
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

    def updatePixelCoordinates(self, gameProgress):
        if self.castCooldownCounter >= self.castCooldown:
            self.castCooldownCounter = 0
            zone = Zone.Zone(self.xBlock - self.spawnRange/2, self.yBlock - self.spawnRange/2, self.xBlock + self.spawnRange/2, self.yBlock + self.spawnRange/2)
            gameProgress.listMobs.spawnMobBulldozer(zone, self)
        super().updatePixelCoordinates(gameProgress)
