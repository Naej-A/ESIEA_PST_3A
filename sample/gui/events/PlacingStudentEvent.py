import pyglet
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.PlacingStudentWidget import PlacingStudentWidget
from sample.gui.widget.SelectStudentWidget import SelectStudentWidget
from pyglet.event import EventDispatcher

class PlacingStudentEvent(EventDispatcher):
    _frame = None
    currentWidgetList = list()
    batchWidget = pyglet.graphics.Batch()
    listTowerToPlace = list()
    currentlistTowerToPlaceLength = None
    precedlistTowerToPlaceLength = None


    @staticmethod
    def drawWidget():
        PlacingStudentEvent.batchWidget.draw()
        for widget in PlacingStudentEvent.currentWidgetList:
            if isinstance(widget,SelectStudentWidget):
                widget.drawComplement()

        PlacingStudentEvent.currentlistTowerToPlaceLength = len(PlacingStudentEvent.listTowerToPlace)
        if PlacingStudentEvent.precedlistTowerToPlaceLength > PlacingStudentEvent.currentlistTowerToPlaceLength:
            widget = PlacingStudentEvent.currentWidgetList.pop(0)
            PlacingStudentEvent._frame.remove_widget(widget)
        PlacingStudentEvent.precedlistTowerToPlaceLength = PlacingStudentEvent.currentlistTowerToPlaceLength


    @staticmethod
    def initWidget():
        counter = 0
        for tower in PlacingStudentEvent.listTowerToPlace:
            PlacingStudentEvent.addWidget(
                SelectStudentWidget(100 + 100 * counter, 10, tower, PlacingStudentEvent.batchWidget))
            counter += 1
        PlacingStudentEvent.addWidget(PlacingStudentWidget(306, 298, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(956, 247, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(270, 487, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(263, 232, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(592, 223, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(95, 418, PlacingStudentEvent.batchWidget))
        PlacingStudentEvent.addWidget(PlacingStudentWidget(613, 364, PlacingStudentEvent.batchWidget))


    @staticmethod
    def resetPlacingStudent():
        for widget in PlacingStudentEvent.currentWidgetList:
            PlacingStudentEvent._frame.remove_widget(widget)
        PlacingStudentEvent.currentWidgetList = list()
        PlacingStudentEvent.listTowerToPlace = list()
        PlacingStudentEvent.batchWidget = pyglet.graphics.Batch()

    # @staticmethod
    # def placeStudent(frame):

    @staticmethod
    def setFrameForWidgets(frame):
        PlacingStudentEvent._frame = frame

    @staticmethod
    def addWidget(widget):
        PlacingStudentEvent._frame.add_widget(widget)
        PlacingStudentEvent.currentWidgetList.append(widget)


    @staticmethod
    def setListTowerToPlace(newTowerList):
        PlacingStudentEvent.listTowerToPlace = newTowerList
        PlacingStudentEvent.currentlistTowerToPlaceLength = len(newTowerList)
        PlacingStudentEvent.precedlistTowerToPlaceLength = len(newTowerList)
        pass

