import pyglet
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.PlacingStudentWidget import PlacingStudentWidget
from pyglet.event import EventDispatcher

class PlacingStudentEvent(EventDispatcher):
    _frame = None
    currentWidgetList = list()
    batchWidget = pyglet.graphics.Batch()

    @staticmethod
    def drawWidget():
        PlacingStudentEvent.batchWidget.draw()

    @staticmethod
    def initWidget():
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
        currentWidgetList = list()
        batchWidget = pyglet.graphics.Batch()

    # @staticmethod
    # def placeStudent(frame):

    @staticmethod
    def setFrameForWidgets(frame):
        PlacingStudentEvent._frame = frame

    @staticmethod
    def addWidget(widget):
        PlacingStudentEvent._frame.add_widget(widget)
        PlacingStudentEvent.currentWidgetList.append(widget)

