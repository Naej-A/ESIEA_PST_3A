import pyglet
import sample.tower.Tower as Tower
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget

# # Create a custom event class that inherits from pyglet.event.Event
def drawTower(tower):
    pathToImage = "ressources/gui/amelioration/amelio_background.png"
    bgImage = pyglet.image.load(pathToImage, file=open(pathToImage, 'rb'))  # Attribution de l'image PNG
    bgImageSprite = pyglet.sprite.Sprite(bgImage, 904, 617)
    bgImageSprite.draw()

    pathToImage = "ressources/gui/amelioration/badges/" + str(tower.year) + "A.png"
    bgImage = pyglet.image.load(pathToImage, file=open(pathToImage, 'rb'))  # Attribution de l'image PNG
    bgImageSprite = pyglet.sprite.Sprite(bgImage, bgImageSprite.x - 15, bgImageSprite.y - 17)
    bgImageSprite.draw()

    DisplayCharacteristics.batchWidget.draw()
    for widget in DisplayCharacteristics.currentWidgetList:
        if isinstance(widget, AmeliorationWidget):
            widget.drawComplement()

    label = pyglet.text.Label(str(tower.name),
                              font_name='Times New Roman',
                              font_size=18,
                              x=bgImageSprite.x + 150, y=bgImageSprite.y + 85,
                              color=(0, 0, 0, 255),
                              anchor_x='left', anchor_y='center')
    label.draw()

    label = pyglet.text.Label("att. " + str(tower.attack) + " | attSpe. " + str(tower.attackSpeed) + " | ran. " + str(
        tower.range) + " | cur. " + str(tower.curiosity),
                              font_name='Times New Roman',
                              font_size=8,
                              x=bgImageSprite.x + 200, y=bgImageSprite.y + 45,
                              # color=(0, 0, 0, 255),
                              anchor_x='left', anchor_y='center')
    label.draw()

    spriteTower = pyglet.sprite.Sprite(tower.image, x=bgImageSprite.x + 60, y=bgImageSprite.y + 50)
    spriteTower.draw()
    pass


class DisplayCharacteristics(pyglet.event.EventDispatcher):
    objectToDetailsOnClick = None
    objectToDetails = None
    _frame = None
    currentWidgetList = list()
    batchWidget = pyglet.graphics.Batch()

    def characteristique(self, object):
        self.dispatch_event('on_showCharacteristique', object)

    @staticmethod
    def drawDetailObject():
        objectToDetails = DisplayCharacteristics.objectToDetails
        objectToDetailsOnClick = DisplayCharacteristics.objectToDetailsOnClick
        if objectToDetails:
            if isinstance(objectToDetails, Tower.Tower):
                tower = DisplayCharacteristics.objectToDetails
                # print(tower)
                drawTower(tower)
                pass

        elif objectToDetailsOnClick:
            if isinstance(objectToDetailsOnClick, Tower.Tower):
                tower = DisplayCharacteristics.objectToDetailsOnClick
                drawTower(tower)
                # print(len(DisplayCharacteristics.currentWidgetList))




    @staticmethod
    def setFrameForWidgets(frame):
        DisplayCharacteristics._frame = frame

    @staticmethod
    def addWidget(widget):
        DisplayCharacteristics._frame.add_widget(widget)
        DisplayCharacteristics.currentWidgetList.append(widget)

    #---------------- custom event ---------------
    def on_showCharacteristique(self, object):
        DisplayCharacteristics.objectToDetails = object
        DisplayCharacteristics.drawDetailObject()


    def on_unShowCharacteristique(self):
        DisplayCharacteristics.objectToDetails = None


    def on_clickShowCharacteristique(self, object):
        DisplayCharacteristics.objectToDetailsOnClick = object
        DisplayCharacteristics.drawDetailObject()

        #### si quand on clique sur l'objet c'est une instance de tower
        if isinstance(object, Tower.Tower):
            x = 904
            y = 617
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 1*77, y - 100, object, object.evolutionBlock[0], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 2*77, y - 100, object, object.evolutionBlock[1], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 3*77, y - 100, object, object.evolutionBlock[2], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 4*77, y - 100, object, object.evolutionBlock[3], DisplayCharacteristics.batchWidget))

    def on_clickUnShowCharacteristique(self, x, y):
        estPasse = False
        for widget in DisplayCharacteristics.currentWidgetList:
            if x >= widget.x and x < widget.x + widget.width and y >= widget.y and y < widget.y + widget.height:
                estPasse = True
        if estPasse:
            pass
        else:
            for widget in DisplayCharacteristics.currentWidgetList:
                DisplayCharacteristics._frame.remove_widget(widget)
            DisplayCharacteristics.objectToDetailsOnClick = None
            DisplayCharacteristics.currentWidgetList = list()
            DisplayCharacteristics.batchWidget = pyglet.graphics.Batch()


DisplayCharacteristics.register_event_type('on_showCharacteristique')
DisplayCharacteristics.register_event_type('on_unShowCharacteristique')
DisplayCharacteristics.register_event_type('on_clickShowCharacteristique')
DisplayCharacteristics.register_event_type('on_clickUnShowCharacteristique')


"""label = pyglet.text.Label(str(objectToDetailsOnClick.name),
                                          font_name='Times New Roman',
                                          font_size=36,
                                          x=200, y=200,
                                          anchor_x='center', anchor_y='center')
                label.draw()"""