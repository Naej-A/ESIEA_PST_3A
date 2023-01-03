import math
import pyglet

class Shoot(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, mobTarget, speed, damage):
        super().__init__(img, xPixel, yPixel)
        self.target = mobTarget
        self.speed = speed
        self.damage = damage
        self.x = xBlock
        self.y = yBlock

    def onHitEffect(self):
        # Fonction à surcharger dans les classes filles pour ajouter des effets lorsque que le tire atteint sa cible
        return None

    def move(self):
        if round(self.x) == round(self.target.xBlock) and round(self.y) == round(self.target.yBlock):
            self.target.hitByShoot(self)
            return False
        else:
            distanceRemaning = math.sqrt(pow(self.target.xBlock - self.x, 2) + pow(self.target.yBlock - self.y, 2))
            self.x = self.x + self.speed * (self.target.xBlock - self.x) / distanceRemaning
            self.y = self.y + self.speed * (self.target.yBlock - self.y) / distanceRemaning
            return True