import pyglet
from sample.gui.GamePhaseEvents import GamePhaseEvents
from pyglet.gui.widgets import PushButton
from sample.GAMEPHASE import GAMEPHASE
from pyglet.gl import *

class AmeliorationWidget(PushButton):
    def __init__(self, xPixel, yPixel, tower, educationField, batch):
        self.tower = tower
        self.educationField = educationField

        if educationField.nameStatToAdd ==  "attack":
            pressedAtt = pyglet.resource.image("ressources/gui/amelioration/background_amelioration/amelioration_attaque.jpg")
        elif educationField.nameStatToAdd ==  "attackSpeed":
            pressedAtt = pyglet.resource.image("ressources/gui/amelioration/background_amelioration/amelioration_attq_speed.jpg")
        elif educationField.nameStatToAdd ==  "range":
            pressedAtt = pyglet.resource.image("ressources/gui/amelioration/background_amelioration/amelioration_Range.jpg")
        elif educationField.nameStatToAdd ==  "curiosity":
            pressedAtt = pyglet.resource.image("ressources/gui/amelioration/background_amelioration/amelioration_Curio.jpg")
        else:
            raise ValueError("the education field don't have the good name")
        super().__init__(x=xPixel, y=yPixel, pressed=pressedAtt, depressed=pressedAtt, hover=pressedAtt, batch=batch, group=None)
        self.set_handler('on_release', self.push_button_handler)




    def push_button_handler(self):
        self.educationField = self.tower.increaseLevelEducationField(self.educationField)
        print(self.tower)


    def drawComplement(self):
        pathToImage = "ressources/gui/amelioration/level_amelio/amelioration_" + str(self.educationField.level) + ".png"
        binary_file_image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        amelioration = pyglet.image.load(pathToImage, file=binary_file_image)  # Attribution de l'image PNG
        sprite =  pyglet.sprite.Sprite(amelioration,self.x + 6, self.y + 21)

        label = pyglet.text.Label(str(self.educationField.price),
                                  font_name='Times New Roman',
                                  font_size=10,
                                  x=self.x + 50, y=self.y + 12,
                                  color=(0,0,0,255),
                                  anchor_x='right', anchor_y='center')
        label.draw()

        sprite.draw()
