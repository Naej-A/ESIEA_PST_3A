import pyglet
from sample.GAMEPHASE import GAMEPHASE
class GamePhaseEvents(pyglet.event.EventDispatcher):

    _gamePhase = GAMEPHASE.STUDENT_SELECT

    def on_changeGamePhase(self, gamePhase):
        GamePhaseEvents._gamePhase = gamePhase
        print(GamePhaseEvents._gamePhase)

    @staticmethod
    def getCurrentGamePhase():
        return GamePhaseEvents._gamePhase

GamePhaseEvents.register_event_type('on_changeGamePhase')