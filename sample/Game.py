from threading import Thread
from time import sleep, perf_counter
import sample.scene.Scene as Scene
import pyglet

class Game:
    def __init__(self, window):
        self.scene = Scene.Scene(window, 60)

def task():
    print('Starting a task...')
    sleep(1)
    print('done')
def task2():
    print('Starting a task...')
    sleep(2)
    print('done')

if __name__ == '__main__':
    window = pyglet.window.Window()
    game = Game(window)

    @window.event
    def on_draw():
        window.clear()
        game.scene.drawScene()


    pyglet.app.run()