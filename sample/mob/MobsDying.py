from sample.mob.Mobs import Mobs
import sample.Zone as Zone
import sample.IsometricTools as IsometricTools

class MobsDying(Mobs):

    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, pv, speed, tear, mobName, scale):
        super().__init__(img, xPixel, yPixel, xBlock, yBlock, pv, speed, tear, mobName, scale)
        if mobName == "Vehicule":
            self.spawnedMobName = "Student"
            self.numberMobsSpawned = 10
            self.spawnRange = 3


    def onDeathEffect(self, gameProgress):
        zone = Zone.Zone(self.xBlock - self.spawnRange / 2, self.yBlock - self.spawnRange / 2, self.xBlock + self.spawnRange / 2, self.yBlock + self.spawnRange / 2)
        for i in range(self.numberMobsSpawned):
            mobSpawned = gameProgress.listMobs.spawnMob(zone, self.spawnedMobName)
            mobSpawned.ipPath = self.idPath
            mobSpawned.idZone = self.idZone
