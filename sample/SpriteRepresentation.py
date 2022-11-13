import pyglet
import errno
import os


class SpriteRepresentation:
    compteur = 0

    def __init__(self, y, x, tabRepresentation, imageName):
        SpriteRepresentation.compteur += 1
        self.id = SpriteRepresentation.compteur

        self.YBaseRelativeCoord = y
        self.XBaseRelativeCoord = x
        self.tabRepresentation = tabRepresentation
        self.tabRepresentation[y][x] = self.id

        self.imageName = imageName
        pathToImage = "../ressources/" + imageName
        if not os.path.isfile(pathToImage): # si l'image n'existe pas lance une erreur
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), imageName)
        file_lecture = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.pygletSprite = pyglet.image.load(pathToImage, file=file_lecture)  # Attribution de l'image PNG
