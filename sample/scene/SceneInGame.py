import pyglet
from sample.GameProgress import GameProgress
from sample.scene.Scene import Scene
from sample.gui.DisplayCharacteristics import DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.NextGamePhaseWidget import NextGamePhaseWidget
from sample.gui.events.EventManagement import EventManagement
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget

#import à retirer ensuite
from sample.tower.Tower import Tower



class SceneInGame(Scene):
    def __init__(self, window, frameRate):
        super().__init__(window, frameRate)
        self.gameReprersentation = GameProgress(50, 50, window.width, window.height)
        self.batchWidget = pyglet.graphics.Batch()
        GamePhaseEvents.setGameScene(self)
        self.frame = None
        self.currentWidgetList = list()
        image = open('ressources/background/Dinguerie.png', 'rb')  # Lecture du fichier en binaire
        self.map = pyglet.image.load('ressources/background/Dinguerie.png', file=image)
        self.pastGamePhase = None



    def addWidget(self, widget):
        self.frame.add_widget(widget)
        self.currentWidgetList.append(widget)

    def initWidgetByGamePhase(self):
        if not self.frame:
            self.frame = pyglet.gui.Frame(self.window, order=6)
            DisplayCharacteristics.setFrameForWidgets(pyglet.gui.Frame(self.window, order=6))
        self.batchWidget = pyglet.graphics.Batch()

        for widget in self.currentWidgetList:
            self.frame.remove_widget(widget)
        self.currentWidgetList = list()

        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            self.addWidget(NextGamePhaseWidget(1100, 100, GAMEPHASE.PLACING_STUDENT, self.batchWidget))
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            nextPhaseWidget = NextGamePhaseWidget(1100, 100, GAMEPHASE.GAME, self.batchWidget)
            self.frame.add_widget(nextPhaseWidget)
            self.currentWidgetList.append(nextPhaseWidget)
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            return

    def drawScene(self):
        self.window.clear()
        self.map.blit(0, 0, 0)
        # print(GamePhaseEvents.getCurrentGamePhase().name)
        self.batchWidget.draw()


        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            return
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            return
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            self.gameReprersentation.afficherTowers()
            self.gameReprersentation.afficherShoots()
            self.gameReprersentation.afficherMobs()
            # if len(self.listMobs.listMobsOnMap) == 0 and len(self.mobToSpawn) == 0:
            #     pyglet.clock.unschedule(self.updateGame)

        DisplayCharacteristics.drawDetailObject()

    def InitCustomEventsByGamePhase(self):
        EventManagement.resetCustomEventStack()
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            for tower in self.gameReprersentation.listTower:
                EventManagement.addEvent(tower)

