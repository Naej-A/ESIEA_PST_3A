import pyglet
from sample.GAMEPHASE import GAMEPHASE

class GamePhaseEvents(pyglet.event.EventDispatcher):

    _gamePhase = GAMEPHASE.STUDENT_SELECT
    _gameScene = None

    @staticmethod
    def setGameScene(gameScene):
        GamePhaseEvents._gameScene = gameScene
        GamePhaseEvents._gameScene.InitCustomEventsByGamePhase()

    def on_changeGamePhase(self, gamePhase):
        GamePhaseEvents._gamePhase = gamePhase
        GamePhaseEvents._gameScene.InitCustomEventsByGamePhase()
        GamePhaseEvents._gameScene.initWidgetByGamePhase()

    @staticmethod
    def getCurrentGamePhase():
        return GamePhaseEvents._gamePhase

GamePhaseEvents.register_event_type('on_changeGamePhase')