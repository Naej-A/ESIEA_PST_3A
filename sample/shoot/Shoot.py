import math
import pyglet
import sample.IsometricTools as IsometricTools

class Shoot(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, xPixel, yPixel, xBlock, yBlock, mobTarget, speed, damage):
        pathToImage = "ressources/Tux.png"
        image = open(pathToImage, 'rb')
        sprit = pyglet.image.load(pathToImage, file=image)
        super().__init__(sprit, xPixel, yPixel)
        self.scale = 0.5
        self.target = mobTarget
        self.speed = speed
        self.damage = damage
        self.xBlock = xBlock
        self.yBlock = yBlock

    def onHitEffect(self):
        # Fonction à surcharger dans les classes filles pour ajouter des effets lorsque que le tire atteint sa cible
        return None

    def move(self):
        self.orientSprite()
        distanceRemaning = math.sqrt(pow(self.target.xBlock - self.xBlock, 2) + pow(self.target.yBlock - self.yBlock, 2))
        if distanceRemaning < self.speed:
            self.target.hitByShoot(self)
            return False
        self.xBlock = self.xBlock + self.speed * (self.target.xBlock - self.xBlock) / distanceRemaning
        self.yBlock = self.yBlock + self.speed * (self.target.yBlock - self.yBlock) / distanceRemaning
        return True

    def orientSprite(self):
        if self.target.yBlock + self.target.xBlock < self.yBlock + self.xBlock:
            self.scale_y = 1
        else:
            self.scale_y = -1

    def updatePixelCoordinates(self, gameProgress):
        self.x, self.y = IsometricTools.coordinateToPixel(gameProgress, self.xBlock, self.yBlock)
        self.x -= self.width / 2
        self.y -= self.height * self.scale_y / 2