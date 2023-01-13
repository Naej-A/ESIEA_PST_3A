#TODO: faire les fonctions rotation horaire et rotation antihoraire
#TODO: faire un affichage de debug correcte car pour l'instant cela marche uniquement avec les maps carré
#TODO: fonction ajoute spriteRepresentation à representationCarte
import random

import sample.ListBlock as lsp
import sample.ListMobs as lm
import pyglet
import sample.IsometricTools as IsometricTools
import sample.Level as lvl
import sample.tower.Tower as Tower
from sample.GAMEPHASE import GAMEPHASE
from sample.SCENESTATE import SCENESTATE
from sample.gui.GamePhaseEvents import GamePhaseEvents


class GameProgress:
    ratioPixel = 14
    estacaTears = 0
    listTowerToPlace = list()

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
        self.PV = 10
        self.listShoot = list()
        self.yearNumber = 0
        self.spawnRate = 0
        self.spawnCounter = 0
        self.mobToSpawn = list()

        self.gamePhaseEventDispasher = GamePhaseEvents()
        self._initTower()
        self.initPhase()


    def _init_carte(self):
        self.representationCarte = []
        for k in range(self.ordonneeY):
            for i in range(self.absysseX):
                a = i + k * self.absysseX  # remplir liste dde nombre croissant (et pas pain au chocolat) (( comme jean pierre pas pain)) (((c'est drole looooool)))
                self.representationCarte.append(0)
        return 0

    def _initTower(self):
        xBlock = 37
        yBlock = 80
        tower = Tower.Tower(0, 0, xBlock, yBlock, "nom")
        tower.updatePixelCoordinates(self)
        self.listTower.append(tower)


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

    def afficherTowers(self):
        self.drawListOfSprite(self.listTower)
        return 0

    def afficherShoots(self):
        self.drawListOfSprite(self.listShoot)
        return 0

    @staticmethod
    def drawListOfSprite(listSprite):
        for sprite in listSprite:
            sprite.draw()


    def afficherMobs(self):
        self.listMobs.order()
        for mob in self.listMobs.listMobsOnMap:
            mob.updatePixelCoordinates(self)
            mob.draw()
        self.listMobs.moveMobs(self.level)

    def initPhase(self):
        # #
        # # # #Choix des étudiants
        # while  SCENESTATE.GAME_RUNNING and self.PV > 0:
        #     while GAMEPHASE.STUDENT_SELECT == GamePhaseEvents.getCurrentGamePhase():
        #         #création des tours
        #         pass
        #     # # # #Positionement des étudiants
        #     while GAMEPHASE.PLACING_STUDENT == GamePhaseEvents.getCurrentGamePhase():
        #         pass
        #
        if GAMEPHASE.STUDENT_SELECT == GamePhaseEvents.getCurrentGamePhase():
            return
        elif GAMEPHASE.PLACING_STUDENT == GamePhaseEvents.getCurrentGamePhase():
            return
        elif GAMEPHASE.GAME == GamePhaseEvents.getCurrentGamePhase():
            self.choseSpawnList()
            pyglet.clock.schedule_interval(self.spawnMob, 0.1)
            pyglet.clock.schedule_interval(self.updateGame, 1/60)
            pyglet.clock.schedule_interval(self.endWave, 1)


    def unInitPhase(self):
        if GAMEPHASE.STUDENT_SELECT == GamePhaseEvents.getCurrentGamePhase():
            return
        elif GAMEPHASE.PLACING_STUDENT == GamePhaseEvents.getCurrentGamePhase():
            for tower in self.listTower:
                GameProgress.listTowerToPlace.append(tower)
                tower.xBlock = 10000000

            return
        elif GAMEPHASE.GAME == GamePhaseEvents.getCurrentGamePhase():
            pyglet.clock.unschedule(self.updateGame)
            pyglet.clock.unschedule(self.endWave)
            for tower in self.listTower:
                if tower.level >= 5:
                    self.listTower.remove(tower)
            self.goNextYear()
            return

    def goNextYear(self):
        self.yearNumber += 1
        for tower in self.listTower:
            tower.studentPassNextYear()


    def spawnMob(self, *args):
        self.spawnCounter += 1
        if self.spawnCounter >= self.spawnRate:
            self.listMobs.spawnMob(self.level.spawningZone, self.mobToSpawn[0])
            self.mobToSpawn = self.mobToSpawn[1:]
        if len(self.mobToSpawn) <= self.yearNumber * 2 - 1:
            self.spawnRate = 1
        if len(self.mobToSpawn) == 0:
            pyglet.clock.unschedule(self.spawnMob)
        return

    def updateGame(self, *args):
        self.listMobs.moveMobs(self.level)
        self.towerShoot()
        self.updateShoot()
        for mob in self.listMobs.listMobsOnMap:
            if mob.pv <= 0:
                mob.onDeathEffect(self)
                GameProgress.estacaTears += mob.tear
                self.listMobs.listMobsOnMap.remove(mob)
        for shoot in self.listShoot:
            if shoot.target not in self.listMobs.listMobsOnMap:
                self.listShoot.remove(shoot)
        return

    def choseSpawnList(self):
        tearToSpend = self.yearNumber * self.yearNumber * 50 + 300
        thisdict = {"Student": 30, "Engineer": 50, "Energic": 60, "GoMuscu": 150, "Vehicule": 500}
        poolMob = list()
        self.mobToSpawn = list()
        for mobName in thisdict.keys():
            if tearToSpend >= thisdict[mobName]:
                poolMob.append(mobName)
        while tearToSpend >= 30:
            mobName = random.choice(poolMob)
            self.mobToSpawn.append(mobName)
            tearToSpend -= thisdict[mobName]
            if tearToSpend < 500:
                for mobName in poolMob:
                    if tearToSpend < thisdict[mobName]:
                        poolMob.remove(mobName)
        self.mobToSpawn.append("Student")
        self.spawnRate = 600/len(self.mobToSpawn)
        self.spawnRate = max(self.spawnRate, 1)
        self.spawnRate = min(self.spawnRate, 50)
        self.spawnCounter = 0

    def towerShoot(self):
        for tower in self.listTower:
            if tower.attackCooldown <= 0:
                if tower.shooting(self):
                    tower.attackCooldown = round(60 / tower.attackSpeed)
            else:
                tower.attackCooldown -= 1

    def updateShoot(self):
        for shoot in self.listShoot:
            if not shoot.move():
                self.listShoot.remove(shoot)
            shoot.updatePixelCoordinates(self)

    def endWave(self, *agrs):
        if self.PV <= 0:
            a = 1
        if len(self.listMobs.listMobsOnMap) == 0 and len(self.mobToSpawn) == 0:
            self.gamePhaseEventDispasher.dispatch_event('on_changeGamePhase', GAMEPHASE.STUDENT_SELECT)

    @staticmethod
    def placeTower(widget):
        tower = GameProgress.listTowerToPlace.pop(0)
        tower.x = widget.x
        tower.y = widget.y
        tower.xBlock, tower.yBlock = IsometricTools.coordinateToPixel2(tower.x, tower.y)

    @staticmethod
    def buy(price):
        if GameProgress.estacaTears >= price:
            GameProgress.estacaTears -= price
            return True
        else:
            return False
