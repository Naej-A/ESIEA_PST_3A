import pyglet
import sample.tower.Tower as Tower

# # Create a custom event class that inherits from pyglet.event.Event
class DisplayCharacteristics(pyglet.event.EventDispatcher):
    objectToDetails = None

    def characteristique(self, object):
        self.dispatch_event('on_showCharacteristique', object)

    @staticmethod
    def drawDetailObject():
        objectToDetails = DisplayCharacteristics.objectToDetails
        if objectToDetails:
            if isinstance(objectToDetails, Tower.Tower):
                print("tower")
                print(objectToDetails.name)
                label = pyglet.text.Label(str(objectToDetails.year),
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

DisplayCharacteristics.register_event_type('on_showCharacteristique')
DisplayCharacteristics.register_event_type('on_unShowCharacteristique')