import random
import pyglet
import errno
import os
import math
class Mobs():
    compteur = 0

    def __init__(self, x, y, pv, speed, mobName, imageName):
        Mobs.compteur += 1
        self.id = Mobs.compteur
        self.x = x
        self.y = y
        self.pv = pv
        self.speed = speed
        self.destinationX = None
        self.destinationY = None
        self.step = 0
        self.mobName = mobName
        self.idPath = None
        self.idZone = -1

        pathToImage = os.getcwd() + "/ressources/" + imageName
        if not os.path.isfile(pathToImage):  # si l'image n'existe pas lance une erreur
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), imageName)
        binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.pygletSprite = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG

    def findDestination(self, path):
        if self.idZone < len(path):
            zone = path[self.idZone]
            self.destinationX = random.randrange(zone.minX, zone.maxX)
            self.destinationY = random.randrange(zone.minY, zone.maxY)
            return True
        return False

    def move(self, level):
        if (round(self.x) == round(self.destinationX) and round(self.y) == round(self.destinationY)):
            self.idZone += 1
            return self.findDestination(level.findPathById(self))
        distanceRemaning = math.sqrt(pow(self.destinationX - self.x, 2) + pow(self.destinationY - self.y, 2))
        self.x = self.x + self.speed * (self.destinationX - self.x) / distanceRemaning
        self.y = self.y + self.speed * (self.destinationY - self.y) / distanceRemaning
        return True


