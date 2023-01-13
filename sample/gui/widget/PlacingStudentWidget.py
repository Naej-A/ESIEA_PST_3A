import pyglet
from sample.gui.GamePhaseEvents import GamePhaseEvents
from pyglet.gui.widgets import PushButton
from sample.GameProgress import GameProgress
from pyglet.gl import *


class PlacingStudentWidget(PushButton):
    def __init__(self, xPixel, yPixel, batch):
        pressedAtt = pyglet.resource.image("ressources/gui/widget/PlacingZone/PlacingZone.png")
        hover = pyglet.resource.image("ressources/gui/widget/PlacingZone/PlacingZoneHoverTest2.png")
        self.isUsed = False

        super().__init__(x=xPixel, y=yPixel, pressed=pressedAtt, depressed=pressedAtt, hover=hover, batch=batch,
                         group=None)
        self.set_handler('on_release', self.push_button_handler)

    def push_button_handler(self):
        if not self.isUsed:
            self.isUsed = GameProgress.placeTower(self)
            self._hover_img = self._pressed_img


