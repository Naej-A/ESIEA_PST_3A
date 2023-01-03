#TODO: faire les fonctions rotation horaire et rotation antihoraire
#TODO: faire un affichage de debug correcte car pour l'instant cela marche uniquement avec les maps carré
#TODO: fonction ajoute spriteRepresentation à representationCarte
import sample.ListBlock as lsp
import sample.ListMobs as lm
import pyglet
import sample.IsometricTools as IsometricTools
import sample.Level as lvl
import sample.tower.Tower as Tower


class GameProgress:
    ratioPixel = 14

    def __init__(self, absysseX, ordonneeY, width_x_window, height_y_window):
        self.absysseX = absysseX
        self.ordonneeY = ordonneeY
        self._init_carte()
        self.positionCamera = 0  # 0 = 0° | 1 = 90° | 2 = 180° | 3 = 270°
        self.listSpriteRepresentation = lsp.ListSpriteRepresentation()
        self.listMobs = lm.ListMobs()
        self.originePixelX = width_x_window / 2
        self.originePixelY = height_y_window
        self.level = lvl.Level()
        self.listTower = list()


        self._initTower()


    def _init_carte(self):
        self.representationCarte = []
        for k in range(self.ordonneeY):
            for i in range(self.absysseX):
                a = i + k * self.absysseX  # remplir liste dde nombre croissant (et pas pain au chocolat) (( comme jean pierre pas pain)) (((c'est drole looooool)))
                self.representationCarte.append(0)
        return 0

    def _initTower(self):
        xBlock = 10
        yBlock = 10
        xPixel, yPixel = IsometricTools.coordinateToPixel(self, xBlock, yBlock)
        self.listTower.append(Tower.Tower(self.listSpriteRepresentation.findSpriteByImageName("UwU_Tower.png").pygletSprite, xPixel, yPixel, xBlock, yBlock, "nom" ))



    # ne marche pas encore il faut choper l'index Y et X pour l'affichage
    def afficheCarteCarreDebug(self):
        if self.absysseX > self.ordonneeY:
            tailleAAfficher = self.absysseX * 2 - 1
        else:
            tailleAAfficher = self.ordonneeY * 2 - 1
        vide = "R=_|"
        vide = "   |"
        for i in range(tailleAAfficher):
            print("|", end="")
            nbCaseVide = abs(tailleAAfficher//2 - i)
            for numVide in range (nbCaseVide):
                print(vide, end="")
            for indexLigneCaseRepresente in range(tailleAAfficher - (2* nbCaseVide) - (tailleAAfficher - (2* nbCaseVide))//2 ):
                index = 0
                if indexLigneCaseRepresente != 0:
                    print(vide, end="")
                print("R="+str(self.representationCarte[0])
                      +"|" , end="")
            for numVide in range (nbCaseVide):
                print(vide, end="")
            print() #newline
        return 0

    def afficheCarteDebug(self):
        print(self.representationCarte)
        print("x=" + str(self.absysseX) + " y=" + str(self.ordonneeY))
        vide = "    |"
        tailleAAfficher = self.absysseX + self.ordonneeY - 1  # Nombre de lignes à afficher
        for i in range(tailleAAfficher):
            print("|", end="")  # print "|" à chaque début de ligne
            for j in range(abs(self.ordonneeY - i - 1)):
                print(vide, end="")  # affiche le bon nombre de "vide" avant d'afficher la map
            for j in range(min(self.absysseX, self.ordonneeY, i+1, tailleAAfficher - i)):  # giga bordel
                if j != 0:
                    print(vide, end="")
                print("R=" + str("%02d" % self.representationCarte[j + max(0, i + 1 - self.ordonneeY) + (i - j - max(0, i + 1 - self.ordonneeY)) * self.absysseX]) + "|", end="")  # affiche la map
            for j in range(abs(tailleAAfficher - (self.ordonneeY + i))):
                print(vide, end="")  # affiche le nombre de vides restant pou compléter
            print()  # retour chariot
        return 0

    def traductionRotation90Antihoraire(self):
        self.positionCamera = self.positionCamera - 1 % 4
        # ------ code pour changer la carte vers -90 -----
        temp = list()
        for x in range(self.absysseX - 1, 0 - 1, -1):
            for y in range(self.ordonneeY):
                temp.append(self.representationCarte[x + y * self.absysseX])
        self.representationCarte = temp
        cache = self.absysseX
        self.absysseX = self.ordonneeY
        self.ordonneeY = cache
        return 0

    def traductionRotation90Horaire(self):
        self.positionCamera = self.positionCamera + 1 % 4
        # ------ code pour changer la carte vers +90 -----
        temp = list()
        for x in range(0, self.absysseX):
            for y in range(self.ordonneeY-1, 0-1, -1):
                temp.append(self.representationCarte[y*self.absysseX + x])
        self.representationCarte = temp
        cache = self.absysseX
        self.absysseX = self.ordonneeY
        self.ordonneeY = cache
        return 0

    def addSpriteToMap(self, idSprite, xMap, yMap):
        sprite = self.listSpriteRepresentation.findSpriteById(idSprite)
        isSpaceFree = True
        for ySprite in range(len(sprite.tabRepresentation)):
            for xSprite in range(len(sprite.tabRepresentation[ySprite])):
                if sprite.tabRepresentation[ySprite][xSprite] != 0:
                    xTot = xSprite - sprite.xBaseRelativeCoord + xMap
                    yTot = ySprite - sprite.yBaseRelativeCoord + yMap
                    if self.representationCarte[xTot + yTot * self.absysseX] != 0:
                        isSpaceFree = False
        if isSpaceFree:
            for ySprite in range(len(sprite.tabRepresentation)):
                for xSprite in range(len(sprite.tabRepresentation[ySprite])):
                    if sprite.tabRepresentation[ySprite][xSprite] != 0:
                        xTot = xSprite - sprite.xBaseRelativeCoord + xMap
                        yTot = ySprite - sprite.yBaseRelativeCoord + yMap
                        self.representationCarte[xTot + yTot * self.absysseX] = sprite.tabRepresentation[ySprite][xSprite]
        return 0

    def deleteSpriteFromMapGraphic(self, xPixel, yPixel):
        xMap, yMap = IsometricTools.pixelToCoordinate(self, xPixel, yPixel)
        idSprite = self.getIdAtIndex(xMap, yMap * self.absysseX)
        if idSprite < 0:
            return -1
        sprite = self.listSpriteRepresentation.findSpriteById(idSprite)
        for ySprite in range(len(sprite.tabRepresentation)):
            for xSprite in range(len(sprite.tabRepresentation[ySprite])):
                if sprite.tabRepresentation[ySprite][xSprite] != 0:
                    xTot = xSprite - sprite.xBaseRelativeCoord + xMap
                    yTot = ySprite - sprite.yBaseRelativeCoord + yMap
                    self.representationCarte[xTot + yTot * self.absysseX] = 0
        return 0

    def getIdAtIndex(self, x, y):
        return self.representationCarte[x + y * self.absysseX]

    def afficherMap(self):
        #  WORK IN PROGRESS
          # Attribution de l'image PNG
        # ------------------ Antoine - Affichage des tours --------------
        self.drawListOfSprite(self.listTower)

        # ------------------ Tom - Affichage de ___ --------------

        # tailleAAfficher = self.absysseX + self.ordonneeY - 1  # Nombre de lignes à afficher
        # for i in range(tailleAAfficher):
        #     for j in range(min(self.absysseX, self.ordonneeY, i+1, tailleAAfficher - i)):  # giga bordel
        #         x = j + max(0, i + 1 - self.ordonneeY)
        #         y = (i - j - max(0, i + 1 - self.ordonneeY))
        #         id = self.getIdAtIndex(x, y)
        #         if id > 0:
        #             x_pixel, y_pixel = IsometricTools.coordinateToPixel(self, x, y)
        #             x_pixel -= self.ratioPixel / 2
        #             y_pixel -= self.ratioPixel * 3 / 4
        #             sprite = self.listSpriteRepresentation.findSpriteById(id)
        #             # x_pixel -= (len(sprite.tabRepresentation[0]) + 1) * MapRepresentation.ratioPixel / 2
        #             pyglet.sprite.Sprite(img=sprite.pygletSprite, y=y_pixel, x=x_pixel).draw()

        #----------------- Fin Tom

        # for y in range(self.ordonneeY):
        #     for x in range(self.absysseX):
        #         id = self.getIdAtIndex(x, y)
        #         if id > 0:
        #
        #             x_pixel,y_pixel = iso.coordinateToPixel(x,y)
        #             sprite = self.listSpriteRepresentation.findSpriteById(id)
        #             x_pixel -= (len(sprite.tabRepresentation[0]) + 1) * MapRepresentation.ratioPixel / 2
        #             pyglet.sprite.Sprite(img=sprite.pygletSprite, y=y_pixel, x=x_pixel).draw()
        return 0

    @staticmethod
    def drawListOfSprite(listSprite):
        for sprite in listSprite:
            print(sprite)
            sprite.draw()


    def afficherMobs(self):
        self.listMobs.order()
        for mob in self.listMobs.listMobsOnMap:
            mob.updatePixelCoordinates(self)
            mob.draw()
        self.listMobs.moveMobs(self.level)

    def playGame(self):

        #Choix des étudiants
        #Positionement des étudiants
        #Boucle de vagues
            #améliorations

        #end game = boite aux lettres reprise
        return None