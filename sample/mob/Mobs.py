import random
import pyglet
import errno
import os
import math
class Mobs:
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

        pathToImage = os.getcwd() + "/ressources/" + imageName
        if not os.path.isfile(pathToImage):  # si l'image n'existe pas lance une erreur
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), imageName)
        binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.pygletSprite = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG

    def changeDestination(self, zone):
        self.destinationX = random.randrange(zone.minX, zone.maxX)
        self.destinationX = random.randrange(zone.minY, zone.maxY)
        return zone

    def move(self, zone):
        if (round(self.x) == round(self.destinationX) and round(self.y) == round(self.destinationY)):
            self.changeDestination(zone)
            return None
        distanceRemaning = math.sqrt(pow(self.destinationX - self.x, 2) + pow(self.destinationY - self.y, 2))
        self.x = self.x + self.speed * (self.destinationX - self.x) / distanceRemaning
        self.y = self.y + self.speed * (self.destinationY - self.y) / distanceRemaning


