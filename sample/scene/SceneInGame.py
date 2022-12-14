import pyglet

import sample.scene.Scene


class SceneInGame(sample.scene.Scene):

    def __init__(self, window, frameRate, gameRepresentation):
        super.__init__(window, frameRate)
        self.gameReprersentation = gameRepresentation

    def _init_widget(self):
        return None

    def drawScene(self):
        super.drawScene()

