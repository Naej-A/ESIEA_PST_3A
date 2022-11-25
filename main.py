import pyglet
from sample import MapRepresentation
from sample import IsometricTools

if __name__ == '__main__':


    map = MapRepresentation.MapRepresentation(10, 10, 1000, 500)
    isoTools = IsometricTools
    x_coord = 145
    y_coord = 55
    print("x_coord = " + str(x_coord) + " | y_coord = " + str(y_coord))
    x_pixel, y_pixel = isoTools.coordinateToPixel(map, x_coord, y_coord)
    print("x_pixel = " + str(x_pixel) + " | y_pixel = " + str(y_pixel))
    x_coord, y_coord = isoTools.pixelToCoordinate(map, x_pixel, y_pixel)
    print("x_coord = " + str(x_coord) + " | y_coord = " + str(y_coord))
    x_pixel, y_pixel = isoTools.coordinateToPixel(map, x_coord, y_coord)
    print("x_pixel = " + str(x_pixel) + " | y_pixel = " + str(y_pixel))
    x_coord, y_coord = isoTools.pixelToCoordinate(map, x_pixel, y_pixel)
    print("x_coord = " + str(x_coord) + " | y_coord = " + str(y_coord))
    x_pixel, y_pixel = isoTools.coordinateToPixel(map, x_coord, y_coord)
    print("x_pixel = " + str(x_pixel) + " | y_pixel = " + str(y_pixel))
    x_coord, y_coord = isoTools.pixelToCoordinate(map, x_pixel, y_pixel)
    print("x_coord = " + str(x_coord) + " | y_coord = " + str(y_coord))
    x_pixel, y_pixel = isoTools.coordinateToPixel(map, x_coord, y_coord)
    print("x_pixel = " + str(x_pixel) + " | y_pixel = " + str(y_pixel))
    x_coord, y_coord = isoTools.pixelToCoordinate(map, x_pixel, y_pixel)
    print("x_coord = " + str(x_coord) + " | y_coord = " + str(y_coord))
    x_pixel, y_pixel = isoTools.coordinateToPixel(map, x_coord, y_coord)
    print("x_pixel = " + str(x_pixel) + " | y_pixel = " + str(y_pixel))
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



