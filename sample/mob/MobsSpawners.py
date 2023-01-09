from sample.mob.Mobs import Mobs
import sample.Zone as Zone

class MobsSpawners(Mobs):

    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, pv, speed, mobName, scale):
        super().__init__(img, xPixel, yPixel, xBlock, yBlock, pv, speed, mobName, scale)
        if mobName == "Engineer":
            self.spawnedMobName = "Bulldozer"
            self.castCooldown = 3 * 60 #Fait spawn un bulldozer toutes les 3 secondes
            self.spawnRange = 2
        self.castCooldownCounter = 0 #Permet de compter 3 secondes

    def move(self, level):
        self.castCooldownCounter += 1
        super().move(level)

    def updatePixelCoordinates(self, gameProgress):
        if self.castCooldownCounter >= self.castCooldown:
            self.castCooldownCounter = 0
            zone = Zone.Zone(self.xBlock - self.spawnRange/2, self.yBlock - self.spawnRange/2, self.xBlock + self.spawnRange/2, self.yBlock + self.spawnRange/2)
            mobSpawned = gameProgress.listMobs.spawnMob(zone, self.spawnedMobName)
            mobSpawned.ipPath = self.idPath
            mobSpawned.idZone = self.idZone
        super().updatePixelCoordinates(gameProgress)
