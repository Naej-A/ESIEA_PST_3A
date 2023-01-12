import random

import pyglet
from pyglet.window import key
from sample.gui.events.EventManagement import EventManagement
from sample import IsometricTools
import numpy as np
import sample.GameProgress as gp
import sample.ListMobs as lm
import sample.gui.DisplayCharacteristics as DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.gui.widget.NextGamePhaseWidget import NextGamePhaseWidget
from sample.GAMEPHASE import GAMEPHASE
from sample.scene.SceneInGame import SceneInGame
from pyglet.window import mouse
from pyglet.gl import *
import sample.shoot.Shoot as Shoot
import sample.mob.Mobs as mob

if __name__ == '__main__':

    # largeur de la fenêtre
    width = 1280
    # hauteur de la fenêtre
    height = 720
    image = pyglet.resource.image('ressources/background/menu_bg.jpeg')
    # titre du de la fenêtre
    title = "Battle for the boîte aux lettres"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre
    EventManagement.setWindow(window)
    gameScene = SceneInGame(window=window, frameRate=60)


    @window.event
    def on_key_press(symbol, modif):
        if symbol == key.ESCAPE:
            print('The escape key was pressed.')
            window.close()

    @window.event
    def on_mouse_press(x, y, button,modifier):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: " + str(y))

    @window.event
    def on_draw():
        window.clear()
        gameScene.drawScene()

    ############## widget ##############
    # gameScene.initWidget(frame)
    ############## fin widget ##########

    frame = gameScene.initWidgetByGamePhase()


    # voir ce qui est inscrit sur
    event_logger = pyglet.window.event.WindowEventLogger()
    # window.push_handlers(event_logger)

    pyglet.app.run()

# ---------------- Minimum with image -------------------
#     window = pyglet.window.Window()
#     image = pyglet.resource.image('ressources/img_Test_1.png')
#     @window.event
#     def on_draw():
#         window.clear()
#         image.blit(100, 100)
#
#     pyglet.app.run()

# ---------------- Minimum with label -------------------
    # window = pyglet.window.Window()
    # label = pyglet.text.Label('Hello, world',
    #                           font_name='Times New Roman',
    #                           font_size=36,
    #                           x=window.width // 2, y=window.height // 2,
    #                           anchor_x='center', anchor_y='center')
    #
    # @window.event
    # def on_draw():
    #     window.clear()
    #     label.draw()
    #
    # pyglet.app.run()
