import pyglet
import sample.tower.Tower as Tower

# # Create a custom event class that inherits from pyglet.event.Event
class DisplayCharacteristics(pyglet.event.EventDispatcher):
    objectToDetailsOnClick = None
    objectToDetails = None

    def characteristique(self, object):
        self.dispatch_event('on_showCharacteristique', object)

    @staticmethod
    def drawDetailObject():
        objectToDetails = DisplayCharacteristics.objectToDetails
        objectToDetailsOnClick = DisplayCharacteristics.objectToDetailsOnClick
        if objectToDetails:
            if isinstance(objectToDetails, Tower.Tower):
                label = pyglet.text.Label(str(objectToDetails.year),
                                          font_name='Times New Roman',
                                          font_size=36,
                                          x=200, y=200,
                                          anchor_x='center', anchor_y='center')
                label.draw()
        elif objectToDetailsOnClick:
            if isinstance(objectToDetailsOnClick, Tower.Tower):
                label = pyglet.text.Label(str(objectToDetailsOnClick.name),
                                          font_name='Times New Roman',
                                          font_size=36,
                                          x=200, y=200,
                                          anchor_x='center', anchor_y='center')
                label.draw()


    def on_showCharacteristique(self, object):
        DisplayCharacteristics.objectToDetails = object
        DisplayCharacteristics.drawDetailObject()


    def on_unShowCharacteristique(self):
        DisplayCharacteristics.objectToDetails = None

    def on_clickShowCharacteristique(self, object):
        DisplayCharacteristics.objectToDetailsOnClick = object
        DisplayCharacteristics.drawDetailObject()

    def on_clickUnShowCharacteristique(self):
        DisplayCharacteristics.objectToDetailsOnClick = None

DisplayCharacteristics.register_event_type('on_showCharacteristique')
DisplayCharacteristics.register_event_type('on_unShowCharacteristique')
DisplayCharacteristics.register_event_type('on_clickShowCharacteristique')
DisplayCharacteristics.register_event_type('on_clickUnShowCharacteristique')