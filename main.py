import pyglet
from sample import GameProgress
from sample import IsometricTools

if __name__ == '__main__':


    map = MapRepresentation.MapRepresentation(10, 10, 1000, 500)
    isoTools = IsometricTools
    # map.afficheCarteDebug()
    # map.addSpriteToMap(1, 5, 5)
    # map.afficheCarteDebug()
    # map.addSpriteToMap(1, 0, 0)
    # map.afficheCarteDebug()
    #
    #
    #
    # window = pyglet.window.Window()
    # image = pyglet.resource.image("ressources/Aubin_le_GOAT.jpg") # Image à afficher
    # label = pyglet.text.Label('Aubin le GOAT', # Text à afficher
    #                           font_name='Comic sans ms',
    #                           font_size=36,
    #                           x=window.width // 2, y=window.height // 2 ,
    #                           anchor_x='center', anchor_y='center')
    # label.color = (255, 0, 255, 255) # Couleur du text
    #
    # @window.event
    # def on_draw():
    #     window.clear()
    #     image.blit((window.width - image.width)/2, (window.height - image.height)/2)
    #     label.draw()
    #
    # pyglet.app.run()



