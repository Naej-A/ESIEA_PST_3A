import pyglet
from sample.GAMEPHASE import GAMEPHASE
class EventManagement:
    eventList = list()
    window = None

    @staticmethod
    def addEvent(anyObject):
        EventManagement.eventList.append(anyObject)
        EventManagement.window.push_handlers(anyObject)

    @staticmethod
    def deleteEvent(anyObject):
        try:
            EventManagement.eventList.remove(anyObject)
        except ValueError:
            return
        EventManagement.window.pop_handlers()
        for obj in EventManagement.eventList:
            EventManagement.window.push_handlers(obj)

    @staticmethod
    def resetCustomEventStack():
        EventManagement.eventList = list()

    @staticmethod
    def setWindow(window):
        EventManagement.window = window



