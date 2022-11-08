import os
import sys

import pyglet
from pyglet.window import key

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':

    window = pyglet.window.Window()
    image = pyglet.resource.image("ressources/Aubin_le_GOAT.jpg") # Image à afficher
    label = pyglet.text.Label('Aubin le GOAT', # Text à afficher
                              font_name='Comic sans ms',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2 ,
                              anchor_x='center', anchor_y='center')
    label.color = (255, 0, 255, 255) # Couleur du text

    @window.event
    def on_draw():
        window.clear()
        image.blit((window.width - image.width)/2, (window.height - image.height)/2)
        label.draw()

    pyglet.app.run()



