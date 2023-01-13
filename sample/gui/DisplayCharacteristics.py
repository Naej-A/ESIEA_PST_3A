import pyglet
import sample.tower.Tower as Tower
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget

# # Create a custom event class that inherits from pyglet.event.Event
def drawTower(tower):

    DisplayCharacteristics.batchWidget.draw()
    for widget in DisplayCharacteristics.currentWidgetList:
        if isinstance(widget, AmeliorationWidget):
            widget.drawComplement()
    for item in DisplayCharacteristics.dictionaryCarac:
        item.draw()



class DisplayCharacteristics(pyglet.event.EventDispatcher):
    objectToDetailsOnClick = None
    objectToDetails = None
    _frame = None
    currentWidgetList = list()
    batchWidget = pyglet.graphics.Batch()
    dictionaryCarac = list()

    def characteristique(self, object):
        self.dispatch_event('on_showCharacteristique', object)

    @staticmethod
    def drawDetailObject():
        objectToDetails = DisplayCharacteristics.objectToDetails
        objectToDetailsOnClick = DisplayCharacteristics.objectToDetailsOnClick
        if objectToDetails:
            if isinstance(objectToDetails, Tower.Tower):
                tower = DisplayCharacteristics.objectToDetails
                drawTower(tower)
                pass

        elif objectToDetailsOnClick:
            if isinstance(objectToDetailsOnClick, Tower.Tower):
                tower = DisplayCharacteristics.objectToDetailsOnClick
                drawTower(tower)




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
        self.initDetailsTower(object)

    def on_unShowCharacteristique(self):
        DisplayCharacteristics.objectToDetails = None


    def on_clickShowCharacteristique(self, object):
        DisplayCharacteristics.objectToDetailsOnClick = object
        DisplayCharacteristics.drawDetailObject()

        #### si quand on clique sur l'objet c'est une instance de tower
        if isinstance(object, Tower.Tower):
            tower = object
            x = 904
            y = 617
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 1*77, y - 100, object, object.evolutionBlock[0], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 2*77, y - 100, object, object.evolutionBlock[1], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 3*77, y - 100, object, object.evolutionBlock[2], DisplayCharacteristics.batchWidget))
            DisplayCharacteristics.addWidget(AmeliorationWidget(x + 4*77, y - 100, object, object.evolutionBlock[3], DisplayCharacteristics.batchWidget))
            self.initDetailsTower(tower)



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

    def initDetailsTower(self, tower):
        pathToImage = "ressources/gui/amelioration/amelio_background.png"
        bgImage = pyglet.image.load(pathToImage, file=open(pathToImage, 'rb'))  # Attribution de l'image PNG
        bgImageSprite = pyglet.sprite.Sprite(bgImage, 904, 617)
        DisplayCharacteristics.dictionaryCarac.append(bgImageSprite)

        pathToImage = "ressources/gui/amelioration/badges/" + str(tower.year) + "A.png"
        bgImage = pyglet.image.load(pathToImage, file=open(pathToImage, 'rb'))  # Attribution de l'image PNG
        badgeSprite = pyglet.sprite.Sprite(bgImage, bgImageSprite.x - 15, bgImageSprite.y - 17)
        DisplayCharacteristics.dictionaryCarac.append(badgeSprite)

        labelTowerName = pyglet.text.Label(str(tower.name),
                                           font_name='Times New Roman',
                                           font_size=18,
                                           x=bgImageSprite.x + 150, y=bgImageSprite.y + 68,
                                           color=(0, 0, 0, 255),
                                           anchor_x='left', anchor_y='center')
        DisplayCharacteristics.dictionaryCarac.append(labelTowerName)

        labelTowerStat = pyglet.text.Label(
            "att. " + str(tower.attack) + " | attSpe. " + str(tower.attackSpeed) + " | ran. " + str(
                tower.range) + " | cur. " + str(tower.curiosity),
            font_name='Times New Roman',
            font_size=9,
            x=bgImageSprite.x + 175, y=bgImageSprite.y + 25,
            color=(0, 0, 0, 255),
            anchor_x='left', anchor_y='center')
        DisplayCharacteristics.dictionaryCarac.append(labelTowerStat)

        labelSlowMo = pyglet.text.Label(
            "SlowMotion",
            font_name='Times New Roman',
            font_size=20,
            x=20, y=700,
            color=(44, 209, 236, 255),
            anchor_x='left', anchor_y='center')
        DisplayCharacteristics.dictionaryCarac.append(labelSlowMo)

        spriteTower = pyglet.sprite.Sprite(tower.image, x=bgImageSprite.x + 50, y=bgImageSprite.y + 20)
        DisplayCharacteristics.dictionaryCarac.append(spriteTower)


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