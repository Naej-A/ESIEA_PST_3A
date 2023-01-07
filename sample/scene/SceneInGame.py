import pyglet
from sample.GameProgress import GameProgress
from sample.scene.Scene import Scene
from sample.gui.DisplayCharacteristics import DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.NextGamePhaseWidget import NextGamePhaseWidget


class SceneInGame(Scene):
    def __init__(self, window, frameRate):
        super().__init__(window, frameRate)
        self.gameReprersentation = GameProgress(50, 50, window.width, window.height)
        self.gameReprersentation.playGame()
        self.batchWidgetSelect = pyglet.graphics.Batch()
        self.batchWidgetPlace = pyglet.graphics.Batch()
        self.batchWidgetGame = pyglet.graphics.Batch()
        for tower in self.gameReprersentation.listTower:
            window.push_handlers(tower)



    def initWidget(self, frame):

        ########### select student widget ###########
        frame.add_widget(NextGamePhaseWidget(300, 0, GAMEPHASE.PLACING_STUDENT, self.batchWidgetSelect ))
        ########### place student widget  ###########
        frame.add_widget(NextGamePhaseWidget(300, 100, GAMEPHASE.GAME, self.batchWidgetPlace ))
        ###########      game widget      ###########


        return None

    def drawScene(self):
        self.window.clear()
        print(GamePhaseEvents.getCurrentGamePhase().name)
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            self.batchWidgetSelect.draw()
            print("est passé")
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            self.batchWidgetPlace.draw()
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            self.batchWidgetGame.draw()
            self.gameReprersentation.afficherMap()
            self.gameReprersentation.afficherMobs()

        DisplayCharacteristics.drawDetailObject()

