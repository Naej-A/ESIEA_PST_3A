import pyglet
import math
from pyglet.window import key
def Draw_map(Map_size):
    Block_vert_lecture = open('ressources/Block_vert.png', 'rb')  # Lecture du fichier en binaire
    Block_vert_image = pyglet.image.load('ressources/Block_vert.png',
                                         file=Block_vert_lecture)  # Attribution de l'image PNG
    Block_vert_sprite = pyglet.sprite.Sprite(img=Block_vert_image)  # création d'un sprite à partir de l'image


    Block_vert_sprite.draw()


if __name__ == '__main__':

    # largeur de la fenêtre
    width = 1000

    # hauteur de la fenêtre
    height = 700

    # titre du de la fenêtre
    title = "Jeu de la mort"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre


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
