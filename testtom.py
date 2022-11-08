import pyglet
import math
from pyglet.window import key


if __name__ == '__main__':

    # largeur de la fenêtre
    width = 1000

    # hauteur de la fenêtre
    height = 700

    # titre du de la fenêtre
    title = "Jeu de la mort"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre

    Aubin_image = pyglet.resource.image('ressources/Aubin_le_GOAT.jpg')  # Image à afficher
    Aubin_sprite = pyglet.sprite.Sprite(img=Aubin_image)  # création d'un sprite à partir de l'image
    Aubin_sprite.x = (window.width - Aubin_sprite.width) / 2
    Aubin_sprite.y = (window.height - Aubin_sprite.height) / 2

    Rond_rouge_lecture = open('ressources/Rond_rouge.png', 'rb')  # Lecture du fichier en binaire
    Rond_rouge_image = pyglet.image.load('ressources/Rond_rouge.png',
                                         file=Rond_rouge_lecture)  # Attribution de l'image PNG

    Rond_rouge_sprite = pyglet.sprite.Sprite(img=Rond_rouge_image)  # création d'un sprite à partir de l'image

    label = pyglet.text.Label('Aubin le GOAT',  # Text à afficher
                              font_name='Cooper',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')
    label.color = (255, 0, 255, 255)  # Couleur du text

    @window.event
    def on_key_press(symbol):
        if symbol == key.A:
            print('The "A" key was pressed.')
        elif symbol == key.LEFT:
            print('The left arrow key was pressed.')
        elif symbol == key.ENTER:
            print('The enter key was pressed.')
        # elif symbol == key.ESCAPE:
        #     print('The escape key was pressed.')
            window.close()
        else:
            print('A key was pressed ')


    from pyglet.window import mouse


    @window.event
    def on_mouse_press(x, y, button):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: " + str(y))

    t = [0]
    def update(dt):
        t[0] += dt
        # Aubin_sprite.x = math.cos(t[0] + math.acos((Aubin_sprite.height / 2) / math.sqrt((Aubin_sprite.x**2 + Aubin_sprite.y**2) / 4))) * math.sqrt((Aubin_sprite.x**2 + Aubin_sprite.y**2) / 4) + (window.width) / 2
        # Aubin_sprite.y = math.sin(t[0] + math.acos((Aubin_sprite.width / 2) / math.sqrt((Aubin_sprite.x**2 + Aubin_sprite.y**2) / 4))) * math.sqrt((Aubin_sprite.x**2 + Aubin_sprite.y**2) / 4) + (window.height) / 2
        # Aubin_sprite.rotation = t[0] * 360 / 7
        Rond_rouge_sprite.x = math.cos(t[0]) * 250 + (window.width - Rond_rouge_sprite.width) / 2
        Rond_rouge_sprite.y = math.sin(t[0]) * 250 + (window.height - Rond_rouge_sprite.height) / 2
        print(t[0])
    # S'actualise 120 fois par secondes
    pyglet.clock.schedule_interval(update, 1 / 120)

    @window.event
    def on_draw():
        window.clear()
        Aubin_sprite.draw()
        Rond_rouge_sprite.draw()
        label.draw()

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
