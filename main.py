import pyglet
from pyglet.window import key


if __name__ == '__main__':
    import pyglet

    window = pyglet.window.Window()
    image = pyglet.resource.image('ressources/Aubin_le_GOAT.jpg') # Imgae à afficher
    label = pyglet.text.Label('Aubin le GOAT', # Text à afficher
                              font_name='Comic sans ms',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2 ,
                              anchor_x='center', anchor_y='center')
    label.color = (255, 0, 255, 255) # Couleur du text

    @window.event # important de savoir que un event peut être surchargé
    def on_key_press(symbol, modifiers):
        print('A key was pressed ')


    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.A:
            print('The "A" key was pressed.')
        elif symbol == key.LEFT:
            print('The left arrow key was pressed.')
        elif symbol == key.ENTER:
            print('The enter key was pressed.')
        elif symbol == key.ESCAPE:
            print('The escape key was pressed.')
            window.close()
        else:
            print('A key was pressed ')


    from pyglet.window import mouse


    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: "+ str(y))

    @window.event
    def on_draw():
        window.clear()
        image.blit((window.width - image.width)/2, (window.height - image.height)/2)
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



