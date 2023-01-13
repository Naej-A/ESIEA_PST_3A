import pyglet
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.DisplayCharacteristics import DisplayCharacteristics
from sample.gui.events.SelectStudentEvents import SelectStudentEvents
from pyglet.gui.widgets import PushButton


class SelectStudentWidget(PushButton):
    def __init__(self, xPixel, yPixel, tower, batch):
        self.tower = tower

        pressed = pyglet.resource.image('ressources/gui/widget/SelectStudentWidget/card_select_tower.png')
        hover = pyglet.resource.image('ressources/gui/widget/SelectStudentWidget/card_select_tower_hoover.png')

        super().__init__(x=xPixel, y=yPixel, pressed=pressed, depressed=pressed, hover=hover, batch=batch, group=None)
        # self.set_handler('on_mouse_motion', self.on_mouse_motion_handler)

        # complement à draw

        self.updatePosComplement()


    def on_mouse_motion(self, x, y, dx, dy):
        super().on_mouse_motion(x,y,dx,dy)
        dc = DisplayCharacteristics()
        if self._check_hit(x,y):
            dc.dispatch_event("on_showCharacteristique", self.tower)
        else:
            dc.dispatch_event("on_unShowCharacteristique")

    def on_mouse_release(self, x, y, buttons, modifiers):
        super(SelectStudentWidget, self).on_mouse_release(x, y, buttons, modifiers)
        SelectStudentEvents.moveStudentWidget(self)

    def updatePosComplement(self):
        pathToImage = "ressources/gui/amelioration/badges/" + str(self.tower.year) + "A.png"
        binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        amelioration = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG
        self.imageBadge = pyglet.sprite.Sprite(amelioration, self.x + 65, self.y - 22)

        self.labelNom = pyglet.text.Label(self.tower.name,
                                          font_name='Times New Roman',
                                          font_size=14,
                                          x=self.x + 50, y=self.y + 30,
                                          color=(0, 0, 0, 255),
                                          anchor_x='left', anchor_y='center')

        self.towerSprite = pyglet.sprite.Sprite(self.tower.image, self.x + 60, self.y + 60)

    def drawComplement(self):
        self.labelNom.draw()
        self.imageBadge.draw()
        self.towerSprite.draw()

