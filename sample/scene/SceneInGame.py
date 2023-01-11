import pyglet
from sample.GameProgress import GameProgress
from sample.scene.Scene import Scene
from sample.gui.DisplayCharacteristics import DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.NextGamePhaseWidget import NextGamePhaseWidget
from sample.gui.events.EventManagement import EventManagement



class SceneInGame(Scene):
    def __init__(self, window, frameRate):
        super().__init__(window, frameRate)
        self.gameReprersentation = GameProgress(50, 50, window.width, window.height)
        self.gameReprersentation.playGame()
        self.batchWidget = pyglet.graphics.Batch()
        GamePhaseEvents.setGameScene(self)
        self.frame = None
        self.currentWidgetList = list()
        image = open('ressources/background/Map.png', 'rb')  # Lecture du fichier en binaire
        self.map = pyglet.image.load('ressources/background/Map.png', file=image)




    def initWidgetByGamePhase(self):
        if not self.frame:
            self.frame = pyglet.gui.Frame(self.window, order=6)
        self.batchWidget = pyglet.graphics.Batch()

        for widget in self.currentWidgetList:
            self.frame.remove_widget(widget)
        self.currentWidgetList = list()

        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            nextPhaseWidget = NextGamePhaseWidget(300, 0, GAMEPHASE.PLACING_STUDENT, self.batchWidget)
            self.frame.add_widget(nextPhaseWidget)
            self.currentWidgetList.append(nextPhaseWidget)
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            nextPhaseWidget = NextGamePhaseWidget(300, 100, GAMEPHASE.GAME, self.batchWidget)
            self.frame.add_widget(nextPhaseWidget)
            self.currentWidgetList.append(nextPhaseWidget)
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            return

    def drawScene(self):
        self.window.clear()
        self.map.blit(0, 0, 0)
        print(GamePhaseEvents.getCurrentGamePhase().name)
        self.batchWidget.draw()
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            return
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            return
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            self.gameReprersentation.afficherMap()
            self.gameReprersentation.afficherMobs()

        DisplayCharacteristics.drawDetailObject()

    def InitCustomEventsByGamePhase(self):
        EventManagement.resetCustomEventStack()
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            for tower in self.gameReprersentation.listTower:
                EventManagement.addEvent(tower)

