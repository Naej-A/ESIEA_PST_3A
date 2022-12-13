import pyglet
import errno
import os


class SpriteRepresentation:
    compteur = 0


    def __init__(self, x, y, tabRepresentation, imageName):
        SpriteRepresentation.compteur += 1
        self.id = SpriteRepresentation.compteur

        self.yBaseRelativeCoord = y
        self.xBaseRelativeCoord = x
        self.tabRepresentation = tabRepresentation
        self.tabRepresentation[y][x] = self.id

        self.imageName = imageName
        pathToImage = os.getcwd() + "/ressources/" + imageName
        if not os.path.isfile(pathToImage): # si l'image n'existe pas lance une erreur
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), imageName)
        binary_file_image =  open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.pygletSprite = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG

#
#  0 | X
# -1 |-1
#