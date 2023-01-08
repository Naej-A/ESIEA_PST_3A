import math
import pyglet

class Shoot(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, xPixel, yPixel, xBlock, yBlock, mobTarget, speed, damage):
        pathToImage = "ressources/knob.png"
        image = open(pathToImage, 'rb')
        sprit = pyglet.image.load(pathToImage, file=image)
        super().__init__(sprit, xPixel, yPixel)
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
        distanceRemaning = math.sqrt(pow(self.target.xBlock - self.x, 2) + pow(self.target.yBlock - self.y, 2))
        if distanceRemaning < self.speed:
            self.target.hitByShoot(self)
            return False
        else:
            self.x = self.x + self.speed * (self.target.xBlock - self.xBlock) / distanceRemaning
            self.y = self.y + self.speed * (self.target.yBlock - self.yBlock) / distanceRemaning
            return True

    def orientSprite(self):
        if self.target.yBlock - self.target.xBlock < self.yBlock - self.xBlock:
            self.scale_x = 1
        else:
            self.scale_x = -1