import random

import pyglet
from pyglet.window import key
from sample import IsometricTools
import numpy as np
import MapGeneration as mg
import sample.MapRepresentation



def draw_map(height_Map, width_Map):
    # largeur de la fenêtre
    width = 1000
    # hauteur de la fenêtre
    height = 700


if __name__ == '__main__':
    # largeur de la fenêtre
    width = 1000
    # hauteur de la fenêtre
    height = 700
    a = 20
    b = 50
    mapRep = sample.MapRepresentation.MapRepresentation(a, b)

    # for y in range(100):
    #     for x in range(100):
    #         rand3 = random.randint(1, 5)
    #         if rand3 == 5:
    #             rand3 = random.randint(1, 5)
    #         mapRep.addSpriteToMap(rand3, x, y)

    # for i in range(10):
    #     rand1 = random.randint(1, 4)
    #     rand2 = random.randint(0, a - 1)
    #     mapRep.addSpriteToMap(rand1, rand2, 0)
    # for j in range(1, b - 1):
    #     for i in range(1, a - 2):
    #         if mapRep.getIdAtIndex(i, j - 1) > 0:
    #             if mapRep.getIdAtIndex(i, j - 1) == 1:
    #                 mapRep.addSpriteToMap(2, i - 1, j)
    #                 mapRep.addSpriteToMap(2, i, j)
    #                 mapRep.addSpriteToMap(2, i + 1, j)
    #             if mapRep.getIdAtIndex(i, j - 1) == 2:
    #                 rand = random.randint(1, 4)
    #                 mapRep.addSpriteToMap(rand, i - 1, j)
    #                 rand = random.randint(1, 4)
    #                 mapRep.addSpriteToMap(rand, i, j)
    #                 rand = random.randint(1, 4)
    #                 mapRep.addSpriteToMap(rand, i + 1, j)
    #             if mapRep.getIdAtIndex(i, j - 1) == 3:
    #                 mapRep.representationCarte[i + j * mapRep.absysseX] = 0
    #             if mapRep.getIdAtIndex(i, j - 1) == 4:
    #                 mapRep.addSpriteToMap(5, i, j)
    #                 if mapRep.getIdAtIndex(i, j - 1) == 5:
    #                     mapRep.addSpriteToMap(5, i, j)
    #             if mapRep.getIdAtIndex(i - 1, j - 1) > 0 and mapRep.getIdAtIndex(i + 1, j - 1) > 0 and mapRep.getIdAtIndex(i - 1, j - 1) !=  mapRep.getIdAtIndex(i + 1, j - 1):
    #                 mapRep.addSpriteToMap(mapRep.getIdAtIndex(i, j - 1), i, j)
    #             else:
    #                 mapRep.addSpriteToMap(mapRep.getIdAtIndex(i, j - 1), i - 1, j)
    #                 mapRep.addSpriteToMap(mapRep.getIdAtIndex(i, j - 1), i, j)
    #                 mapRep.addSpriteToMap(mapRep.getIdAtIndex(i, j - 1), i + 1, j)

    # mapRep.addSpriteToMap(10, 50, 40)
    # for i in range(100):
    #     for j in range(100):
    #         if (i*j)**2 % 99 == 0:
    #             mapRep.addSpriteToMap(5, i, j)
    # for i in range(500):
    #     rand1 = random.randint(0, 97)
    #     rand2 = random.randint(0, 97)
    #     rand3 = random.randint(6, 9)
    #     mapRep.addSpriteToMap(rand3, rand1, rand2)
    # for i in range(500):
    #     rand1 = random.randint(10, 89)
    #     rand2 = random.randint(10, 89)
    #     mapRep.addSpriteToMap(5, rand1, rand2)
    for i in range(b):
        for j in range(a):
            rand3 = random.randint(1, 4)
            mapRep.addSpriteToMap(rand3, j, i)
    mapRep.afficheCarteDebug()


    # titre du de la fenêtre
    title = "Jeu de la mort"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre

    # Block_vert
    Block_vert_lecture = open('ressources/Block_vert.png', 'rb')  # Lecture du fichier en binaire
    Block_vert_image = pyglet.image.load('ressources/Block_vert.png',
                                         file=Block_vert_lecture)  # Attribution de l'image PNG

    # Block_rouge
    Block_rouge_lecture = open('ressources/Block_rouge.png', 'rb')  # Lecture du fichier en binaire
    Block_rouge_image = pyglet.image.load('ressources/Block_rouge.png',
                                         file=Block_rouge_lecture)  # Attribution de l'image PNG

    # Block_bleu
    Block_bleu_lecture = open('ressources/Block_bleu.png', 'rb')  # Lecture du fichier en binaire
    Block_bleu_image = pyglet.image.load('ressources/Block_bleu.png',
                                         file=Block_bleu_lecture)  # Attribution de l'image PNG


    # Gros_block_color
    Gros_block_color_lecture = open('ressources/Gros_block_color.png', 'rb')  # Lecture du fichier en binaire
    Gros_block_color_image = pyglet.image.load('ressources/Gros_block_color.png',
                                               file=Gros_block_color_lecture)  # Attribution de l'image PNG

    x = 100  # Dimension x de la map
    y = 100  # Dimension y de la map
    z = 4  # Dimension z de la map

    map = np.zeros((z, y, x))  # Création d'un tableau de dimension x, y, z
    mg.picos(map, 3, 1/200)


    @window.event
    def on_key_press(symbol):
        if symbol == key.ESCAPE:
            print('The escape key was pressed.')
            window.close()

    from pyglet.window import mouse


    @window.event
    def on_mouse_press(x, y, button):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: " + str(y))


    @window.event
    def on_draw():
        window.clear()
        mapRep.afficherMap()
        # for zi in range (z):
        #     for yi in range(y):
        #         for xi in range(x):
        #             if map[zi, yi, xi] == 1:
        #                 x_pixel, y_pixel = isoTools.coordinate_to_pixel_z(xi-16, yi-16, zi)
        #                 if x_pixel >= 0 and x_pixel <= window.width-30 and y_pixel-zi*15 >= 0 and y_pixel <= window.height-23:
        #                     if zi == 0:
        #                         temp = pyglet.sprite.Sprite(img=Block_vert_image, y=y_pixel, x=x_pixel)
        #                     elif zi == 1:
        #                         temp = pyglet.sprite.Sprite(img=Block_bleu_image, y=y_pixel, x=x_pixel)
        #                     elif zi == 2:
        #                         temp = pyglet.sprite.Sprite(img=Block_rouge_image, y=y_pixel, x=x_pixel)
        #                     elif zi == 3:
        #                         temp = pyglet.sprite.Sprite(img=Block_vert_image, y=y_pixel, x=x_pixel)
        #                     temp.draw()


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
