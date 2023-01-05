import random

import pyglet
from pyglet.window import key
from sample import IsometricTools
import numpy as np
import sample.GameProgress as gp
import sample.ListMobs as lm
import sample.gui.DisplayCharacteristics as DisplayCharacteristics


def draw_map(height_Map, width_Map):
    # largeur de la fenêtrep
    width = 1000
    # hauteur de la fenêtre
    height = 700


if __name__ == '__main__':

    # largeur de la fenêtre
    width = 1000
    # hauteur de la fenêtre
    height = 700

    # titre du de la fenêtre
    title = "Jeu de la mort"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre

    mapRep = gp.GameProgress(50, 50, width, height)
    # mapRep.addSpriteToMap(10, 20, 40)
    # for i in range(100):
    #     for j in range(100):
    #         if (i*j)**2 % 100 == 0:
    #             mapRep.addSpriteToMap(5, i, j)
    # for i in range(500):
    #     rand1 = random.randint(0, 67)
    #     rand2 = random.randint(0, 67)
    #     rand3 = random.randint(6, 9)
    #     mapRep.addSpriteToMap(rand3, rand1, rand2)
    # for i in range(500):
    #     rand1 = random.randint(10, 59)
    #     rand2 = random.randint(10, 59)
    #     mapRep.addSpriteToMap(5, rand1, rand2)

    for i in range (50*50):
        rand3 = random.randint(2, 2)
        mapRep.addSpriteToMap(rand3,i%50,i//50)
    mapRep.afficheCarteDebug()

    mobToSpawn = {"Student": 50, "Energic": 50, "Engineer": 50, "GoMuscu": 50, "Vehicule":50}


    mapRep.listMobs.spawnMultipleMobs(mapRep.level, mobToSpawn)
    print("affichage coords mobs")
    for i in range(len(mapRep.listMobs.listMobsOnMap)):
        print("x=" + str(mapRep.listMobs.listMobsOnMap[i].xBlock) + " y=" + str(mapRep.listMobs.listMobsOnMap[i].yBlock))







    @window.event
    def on_key_press(symbol, modif):
        if symbol == key.ESCAPE:
            print('The escape key was pressed.')
            window.close()

    from pyglet.window import mouse


    @window.event
    def on_mouse_press(x, y, button,modifier):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: " + str(y))


    @window.event
    def on_draw():
        window.clear()
        mapRep.afficherMap()
        mapRep.afficherMobs()
        DisplayCharacteristics.DisplayCharacteristics.drawDetailObject()

    # voir ce qui est inscrit sur
    event_logger = pyglet.window.event.WindowEventLogger()
    window.push_handlers(event_logger)
    for tower in mapRep.listTower:
        window.push_handlers(tower)
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
