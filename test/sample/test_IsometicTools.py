import sample.IsometricTools as IsometricTools
import sample.MapRepresentation as MapRepresentation
import pytest
import pytest_mock
from unittest.mock import patch
from unittest.mock import MagicMock



@patch('sample.MapRepresentation.MapRepresentation')
def test_coordinateToPixel(mockMapRepresentation):
    width = 1000
    height = 1000
    mapRep = MapRepresentation.MapRepresentation(10,10,width,height)
    mapRep.ratioPixel = 10
    mapRep.originePixelX = 0
    mapRep.originePixelY = 0

    assert mockMapRepresentation.called
    assert mapRep is mockMapRepresentation()

    resultPixelX,resultpixelY = IsometricTools.coordinateToPixel(mapRep,0,0)
    assert resultPixelX == 0 and resultpixelY == 0

    resultPixelX,resultpixelY = IsometricTools.coordinateToPixel(mapRep,1,0)
    assert resultPixelX == 5 and resultpixelY == -2.5

    resultPixelX,resultpixelY = IsometricTools.coordinateToPixel(mapRep,-1,0)
    assert resultPixelX == -5 and resultpixelY == 2.5

    resultPixelX,resultpixelY = IsometricTools.coordinateToPixel(mapRep,0,1)
    assert resultPixelX == -5 and resultpixelY == -2.5

    resultPixelX,resultpixelY = IsometricTools.coordinateToPixel(mapRep,0,-1)
    assert resultPixelX == 5 and resultpixelY == 2.5

@patch('sample.MapRepresentation.MapRepresentation')
def test_pixelToCoordinate(mockMapRepresentation):
    width = 1000
    height = 1000
    mapRep = MapRepresentation.MapRepresentation(10,10,width,height)
    mapRep.ratioPixel = 10
    mapRep.originePixelX = 0
    mapRep.originePixelY = 0

    assert mockMapRepresentation.called
    assert mapRep is mockMapRepresentation()

    x_coord, y_coord = IsometricTools.pixelToCoordinate(mapRep, 0, 0)
    assert x_coord == 0 and y_coord == 0

    resultPixelX, resultpixelY = IsometricTools.pixelToCoordinate(mapRep, 5, -2.5)
    assert resultPixelX == 1 and resultpixelY == 0

    # resultPixelX, resultpixelY = IsometricTools.coordinateToPixel(mapRep, -1, 0)
    # assert resultPixelX == -5 and resultpixelY == 2.5
    #
    # resultPixelX, resultpixelY = IsometricTools.coordinateToPixel(mapRep, 0, 1)
    # assert resultPixelX == -5 and resultpixelY == -2.5
    #
    # resultPixelX, resultpixelY = IsometricTools.coordinateToPixel(mapRep, 0, -1)
    # assert resultPixelX == 5 and resultpixelY == 2.5
    #