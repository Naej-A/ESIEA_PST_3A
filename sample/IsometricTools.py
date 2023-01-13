def coordinateToPixel(mapRep, x_coord, y_coord):
    x_pixel = 0.5 * mapRep.ratioPixel * (x_coord - y_coord) + mapRep.originePixelX
    print("opx"+str(mapRep.originePixelX))
    print("opy"+str(mapRep.originePixelY))

    # x_pixel = l'origine + la moitié de la largeur du block * x_coord - la moitié de la largeur du block * y_coord

    y_pixel = -0.25 * mapRep.ratioPixel * (x_coord + y_coord) + mapRep.originePixelY - mapRep.ratioPixel / 4

    # y_pixel = l'origine - le quarte de la hauteur du block * x_coord -e quarte de la hauteur du block * y_coord

    return x_pixel, y_pixel

def pixelToCoordinate(mapRep, x_pixel, y_pixel):

    x_coord = (2 * (x_pixel - mapRep.originePixelX) / mapRep.ratioPixel - 4 * (y_pixel + mapRep.ratioPixel / 4 - mapRep.originePixelY) / mapRep.ratioPixel) / 2
    # x_coord = (x_pixel - l'origine) / la moitié de la largeur du block - (y_pixel - l'origine) / le quart de la hauteur du block
    y_coord = (- 2 * (x_pixel - mapRep.originePixelX) / mapRep.ratioPixel - 4 * (y_pixel + mapRep.ratioPixel / 4 - mapRep.originePixelY) / mapRep.ratioPixel) / 2
    # y_coord = - ((x_pixel - l'origine) / la moitié de la largeur du block) - (y_pixel - l'origine) / le quart de la hauteur du block

    return x_coord, y_coord

def coordinate_to_pixel_z(mapRep, x_coord, y_coord, z_coord):
    x_pixel = 0.5 * mapRep.ratioPixel * (x_coord - y_coord) + mapRep.originePixelX
    # x_pixel = l'origine + la moitié de la largeur du block * x_coord - la moitié de la largeur du block * y_coord
    y_pixel = mapRep.ratioPixel * (0.5 * z_coord - 0.25 * (x_coord + y_coord)) + mapRep.originePixelY
    # y_pixel = l'origine + la moitié de la hauteur du block * z_coord - le quarte de la hauteur du block * x_coord - le quarte de la hauteur du block * y_coord

    return x_pixel, y_pixel

def pixelToCoordinate2(x_pixel, y_pixel):

    x_coord = (2 * (x_pixel - 640) / 14 - 4 * (y_pixel + 14 / 4 - 720) / 14) / 2
    # x_coord = (x_pixel - l'origine) / la moitié de la largeur du block - (y_pixel - l'origine) / le quart de la hauteur du block
    y_coord = (- 2 * (x_pixel - 640) / 14 - 4 * (y_pixel + 14 / 4 - 720) / 14) / 2
    # y_coord = - ((x_pixel - l'origine) / la moitié de la largeur du block) - (y_pixel - l'origine) / le quart de la hauteur du block

    return x_coord, y_coord