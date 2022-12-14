import pyglet
class Scene:

    def __init__(self, window, frameRate):
        self.window = window
        self.frameRate = frameRate
        self.listWidget = list()

    def drawScene(self):
        image = pyglet.resource.image('Aubin_le_GOAT.jpg')
        image.blit(100,100)

    def _init_widget(self):
        return None


