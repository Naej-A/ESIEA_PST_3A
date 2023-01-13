#TODO: faire les fonctions rotation horaire et rotation antihoraire
#TODO: faire un affichage de debug correcte car pour l'instant cela marche uniquement avec les maps carré
#TODO: fonction ajoute spriteRepresentation à representationCarte
import random

import sample.ListMobs as lm
import pyglet
import sample.IsometricTools as IsometricTools
import sample.Level as lvl
import sample.tower.Tower as Tower
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.Economy import Economy


class GameProgress:
    ratioPixel = 14
    listTowerToPlace = list()

    def __init__(self, absysseX, ordonneeY, width_x_window, height_y_window):
        self.absysseX = absysseX
        self.ordonneeY = ordonneeY
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
        self.initPhase()

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
        self.listMobs.moveMobs(self)

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
        if GAMEPHASE.MENU == GamePhaseEvents.getCurrentGamePhase():
            return
        elif GAMEPHASE.PLACING_STUDENT == GamePhaseEvents.getCurrentGamePhase():
            self.hiring()
            for tower in self.listTower:
                GameProgress.listTowerToPlace.append(tower)
                tower.xBlock = 10000000
                tower.updatePixelCoordinates(self)
            return
        elif GAMEPHASE.GAME == GamePhaseEvents.getCurrentGamePhase():
            self.choseSpawnList()
            pyglet.clock.schedule_interval(self.spawnMob, 0.1)
            pyglet.clock.schedule_interval(self.updateGame, 1/60)
            pyglet.clock.schedule_interval(self.endWave, 1)


    def unInitPhase(self):
        if GAMEPHASE.MENU == GamePhaseEvents.getCurrentGamePhase():
            return
        elif GAMEPHASE.PLACING_STUDENT == GamePhaseEvents.getCurrentGamePhase():

            return
        elif GAMEPHASE.GAME == GamePhaseEvents.getCurrentGamePhase():
            pyglet.clock.unschedule(self.updateGame)
            pyglet.clock.unschedule(self.endWave)
            for tower in self.listTower:
                if tower.year >= 5:
                    self.listTower.remove(tower)
            self.goNextYear()
            Economy.estacaTears += 300

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
            self.spawnCounter = 0
        if len(self.mobToSpawn) <= self.yearNumber * 2 - 1:
            self.spawnRate = 1
        if len(self.mobToSpawn) == 0:
            pyglet.clock.unschedule(self.spawnMob)
        return

    def updateGame(self, *args):
        self.listMobs.moveMobs(self)
        self.towerShoot()
        self.updateShoot()
        for mob in self.listMobs.listMobsOnMap:
            if mob.pv <= 0:
                mob.onDeathEffect(self)
                Economy.estacaTears += mob.tear
                self.listMobs.listMobsOnMap.remove(mob)
        for shoot in self.listShoot:
            if shoot.target not in self.listMobs.listMobsOnMap:
                self.listShoot.remove(shoot)
        if self.PV <= 0:
            self.gamePhaseEventDispasher.dispatch_event("on_changeGamePhase",GAMEPHASE.GAMEOVER)

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
        print(self.spawnRate)
        self.spawnCounter = 0

    def towerShoot(self):
        for tower in self.listTower:
            print(tower)
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

    def hiring(self):
        self.listTower.append(Tower.Tower(0, 0, 1000000, 0, "Patricks"))
        prestige = 0
        for tower in self.listTower:
            prestige += tower.year
        if prestige >= random.randint(1, 50):
            self.listTower.append(Tower.Tower(0, 0, 1000000, 0, "Super Patrick"))

    @staticmethod
    def placeTower(widget):
        if GameProgress.listTowerToPlace:
            tower = GameProgress.listTowerToPlace.pop(0)
            tower.x = widget.x + 33
            tower.y = widget.y + 14
            tower.xBlock, tower.yBlock = IsometricTools.pixelToCoordinate2(tower.x, tower.y)
            tower.x -= tower.width * tower.scale_x/2
            return True
        else:
            return False


