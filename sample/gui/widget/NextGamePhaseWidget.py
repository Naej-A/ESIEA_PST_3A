import pyglet
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from pyglet.gui.widgets import PushButton


class NextGamePhaseWidget(PushButton):
    def __init__(self, xPixel, yPixel, nextGamePhase, batch):
        if not isinstance(nextGamePhase, GAMEPHASE):
            raise ValueError("not a GAMEPHASE object")

        self.gamePhase = nextGamePhase
        if nextGamePhase == GAMEPHASE.PLACING_STUDENT:
            pressed = pyglet.resource.image('ressources/gui/widget/NextGamePhaseWidget/jouer.png')
            hover = pyglet.resource.image('ressources/gui/widget/NextGamePhaseWidget/jouer_HOOVER.png')
        elif nextGamePhase == GAMEPHASE.GAME:
            pressed = pyglet.resource.image('ressources/gui/widget/NextGamePhaseWidget/ready_to_fight.png')
            hover = pyglet.resource.image('ressources/gui/widget/NextGamePhaseWidget/ready_to_fight_HOOVER.png')
        else:
            raise ValueError("GAMEPHASE object is neither GAME or PLACING_STUDENT")

        super().__init__(x=xPixel, y=yPixel, pressed=pressed, depressed=pressed, hover=hover, batch=batch, group=None)
        self.set_handler('on_release', self.push_button_handler)


    def push_button_handler(self):
        gpe = GamePhaseEvents()
        gpe.dispatch_event("on_changeGamePhase", self.gamePhase)


