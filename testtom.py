import random

import pyglet
from pyglet.window import key
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

    gameScene = SceneInGame(window=window, frameRate=60)





    """
    mapRep = gp.GameProgress(50, 50, width, height)

    for i in range (50*50):
        rand3 = random.randint(2, 2)
        mapRep.addSpriteToMap(rand3,i%50,i//50)

    mobToSpawn = {"Student": 50, "Energic": 50, "Engineer": 50, "GoMuscu": 50, "Vehicule":50}


    mapRep.listMobs.spawnMultipleMobs(mapRep.level, mobToSpawn)
    print("affichage coords mobs")
    for i in range(len(mapRep.listMobs.listMobsOnMap)):
        print("x=" + str(mapRep.listMobs.listMobsOnMap[i].xBlock) + " y=" + str(mapRep.listMobs.listMobsOnMap[i].yBlock))
    """

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
    frame = pyglet.gui.Frame(window, order=6)
    gameScene.initWidget(frame)
    ############## fin widget ##########



    # voir ce qui est inscrit sur
    event_logger = pyglet.window.event.WindowEventLogger()
    window.push_handlers(event_logger)
    # for tower in mapRep.listTower:
    #     window.push_handlers(tower)
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
