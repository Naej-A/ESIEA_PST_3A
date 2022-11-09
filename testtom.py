import pyglet
import math
from pyglet.window import key
import IsometricTools
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


    # titre du de la fenêtre
    title = "Jeu de la mort"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre

    Block_vert_lecture = open('ressources/Block_vert.png', 'rb')  # Lecture du fichier en binaire
    Block_vert_image = pyglet.image.load('ressources/Block_vert.png',
                                         file=Block_vert_lecture)  # Attribution de l'image PNG

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
        isoTools = IsometricTools.IsometricTools(height_window=height, width_window=width)
        for y in range(50):
            for x in range(50):
                x_pixel, y_pixel = isoTools.coordinate_to_pixel(x, y)
                if x_pixel >= 0 and x_pixel <= window.width-30 and y_pixel >= 0 and y_pixel <= window.height:
                    temp = pyglet.sprite.Sprite(img=Block_vert_image, y=y_pixel, x=x_pixel)
                    temp.draw()


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
