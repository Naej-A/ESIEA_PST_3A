import random

import pyglet
from pyglet.window import key
from sample.gui.events.EventManagement import EventManagement
from sample import IsometricTools
import numpy as np
import sample.GameProgress as gp
import sample.ListMobs as lm
import sample.gui.DisplayCharacteristics as DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.scene.SceneInGame import SceneInGame
from pyglet.window import mouse
from pyglet.gl import *
from sample.GAMEPHASE import GAMEPHASE
import sample.shoot.Shoot as Shoot
import sample.mob.Mobs as mob

if __name__ == '__main__':
    song = pyglet.resource.media('ressources/Musique/Complots.mp3', streaming=False)
    song.play()
    pyglet.clock.schedule_interval(song.play, song.duration)
    gamePhaseEvent = GamePhaseEvents()
    # largeur de la fenêtre
    width = 1280
    # hauteur de la fenêtre
    height = 720
    image = pyglet.resource.image('ressources/background/menu_bg.jpeg')
    # titre du de la fenêtre
    title = "Battle for the boîte aux lettres"

    window = pyglet.window.Window(width, height, title)  # Création de la fenêtre

    EventManagement.setWindow(window)
    gameScene = SceneInGame(window=window, frameRate=60)


    @window.event
    def on_key_press(symbol, modif):
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.MENU:
            gamePhaseEvent.dispatch_event("on_changeGamePhase", GAMEPHASE.PLACING_STUDENT)
        if symbol == key.ESCAPE:
            print('The escape key was pressed.')
            window.close()
        if symbol == key.R and GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAMEOVER:
            gamePhaseEvent.dispatch_event("on_changeGamePhase", GAMEPHASE.GAMEOVER)
            window.close()

    @window.event
    def on_mouse_press(x, y, button,modifier):
        if button == mouse.LEFT:
            print('The left mouse button was pressed. X: ' + str(x) + " Y: " + str(y))

    @window.event
    def on_draw():
        window.clear()
        gameScene.drawScene()

    frame = gameScene.initWidgetByGamePhase()

    pyglet.app.run()

