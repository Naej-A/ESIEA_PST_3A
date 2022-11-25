import pyglet
import errno
import os
class Mobs:
    compteur = 0

    def __init__(self, x, y, pv, speed, mobName):
        Mobs.compteur += 1
        self.id = Mobs.compteur
        self.blockX = x
        self.blockY = y
        self.pv = pv
        self.speed = speed
        self.mobName = mobName

        pathToImage = os.getcwd() + "/ressources/" + mobName
        if not os.path.isfile(pathToImage):  # si l'image n'existe pas lance une erreur
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), mobName)
        binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.pygletSprite = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG
