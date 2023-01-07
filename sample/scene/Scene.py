import pyglet

class Scene:

    def __init__(self, window, frameRate):
        # if not isinstance(window, pyglet.window):
        #     raise ValueError("window should be a pygle.window object")
        self.window = window
        self.frameRate = frameRate
        self.backgroundImage = pyglet.resource.image('ressources/background/menu_bg.jpeg')
        self.listWidget = list()

    def drawScene(self):
        self.window.clear()
        self.backgroundImage.blit(0,0)

    def initWidget(self, frame):
        return None

    def _init_scene(self):
        return None


