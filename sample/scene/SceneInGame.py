import pyglet
from sample.GameProgress import GameProgress
from sample.scene.Scene import Scene
from sample.gui.DisplayCharacteristics import DisplayCharacteristics
from sample.gui.GamePhaseEvents import GamePhaseEvents
from sample.GAMEPHASE import GAMEPHASE
from sample.gui.widget.NextGamePhaseWidget import NextGamePhaseWidget
from sample.gui.events.EventManagement import EventManagement
from sample.gui.widget.AmeliorationWidget import AmeliorationWidget
from sample.gui.events.PlacingStudentEvent import PlacingStudentEvent
#import à retirer ensuite
from sample.tower.Tower import Tower
from sample.Economy import Economy

from sample.gui.events.PlacingStudentEvent import PlacingStudentEvent





class SceneInGame(Scene):
    def __init__(self, window, frameRate):
        super().__init__(window, frameRate)
        self.gameReprersentation = GameProgress(50, 50, window.width, window.height)
        self.batchWidget = pyglet.graphics.Batch()
        GamePhaseEvents.setGameScene(self)
        self.frame = None
        self.currentWidgetList = list()
        image = open('ressources/background/Dinguerie.png', 'rb')  # Lecture du fichier en binaire
        self.map = pyglet.image.load('ressources/background/Dinguerie.png', file=image)
        self.pastGamePhase = None
        image = open('ressources/Tears.png', 'rb')  # Lecture du fichier en binaire
        sprit = pyglet.image.load('ressources/Tears.png', file=image)
        self.spritTears = pyglet.sprite.Sprite(sprit, 20, 650)
        image = open('ressources/PV.png', 'rb')  # Lecture du fichier en binaire
        sprit = pyglet.image.load('ressources/PV.png', file=image)
        self.spritPV = pyglet.sprite.Sprite(sprit, 20, 600)
        self.spritPV.scale = 2
        image = open('ressources/background/menu_bg.jpeg', 'rb')  # Lecture du fichier en binaire
        self.gameOverBackground = pyglet.image.load('ressources/background/menu_bg.jpeg', file=image)



    def addWidget(self, widget):
        self.frame.add_widget(widget)
        self.currentWidgetList.append(widget)

    def initWidgetByGamePhase(self):
        if not self.frame:
            self.frame = pyglet.gui.Frame(self.window, order=6)
            DisplayCharacteristics.setFrameForWidgets(pyglet.gui.Frame(self.window, order=6))
            PlacingStudentEvent.setFrameForWidgets(pyglet.gui.Frame(self.window, order=6))
        self.batchWidget = pyglet.graphics.Batch()
        PlacingStudentEvent.resetPlacingStudent()

        for widget in self.currentWidgetList:
            self.frame.remove_widget(widget)
        self.currentWidgetList = list()

        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.MENU:
            self.addWidget(NextGamePhaseWidget(1100, 100, GAMEPHASE.PLACING_STUDENT, self.batchWidget))
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            self.addWidget(NextGamePhaseWidget(1100, 100, GAMEPHASE.PLACING_STUDENT, self.batchWidget))
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            nextPhaseWidget = NextGamePhaseWidget(1100, 100, GAMEPHASE.GAME, self.batchWidget)
            PlacingStudentEvent.setListTowerToPlace(self.gameReprersentation.listTowerToPlace)
            PlacingStudentEvent.initWidget()

            self.frame.add_widget(nextPhaseWidget)
            self.currentWidgetList.append(nextPhaseWidget)
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            return

    def drawScene(self):
        self.window.clear()
        self.map.blit(0, 0, 0)
        self.batchWidget.draw()
        self.spritTears.draw()
        self.spritPV.draw()
        tearsNumber = pyglet.text.Label(str(Economy.estacaTears),
            font_name='Times New Roman',
            font_size=25,
            x=55, y=664,
            color=(255, 0, 0, 255),
            anchor_x='left', anchor_y='center')
        tearsNumber.draw()
        PV = pyglet.text.Label(str(self.gameReprersentation.PV),
                                        font_name='Times New Roman',
                                        font_size=25,
                                        x=55, y=614,
                                        color=(255, 0, 0, 255),
                                        anchor_x='left', anchor_y='center')
        PV.draw()


        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.MENU:
            self.gameOverBackground.blit(0, 0, 0)
            text = pyglet.text.Label("Défendez LA boîte aux lettres sacrée arrachée des mains\nde ces êtres impure que sont les étudiants de l'ESTACA.",
                                         font_name='Times New Roman',
                                         font_size=15,
                                         x=200, y=100,
                                         color=(0, 0, 0, 255),
                                         anchor_x='left', anchor_y='center')
            text.draw()
            text = pyglet.text.Label(
                "Appuyez sur n'importe quelle touche pour lancer le jeu",
                font_name='Times New Roman',
                font_size=15,
                x=430, y=600,
                color=(0, 0, 0, 255),
                anchor_x='left', anchor_y='center')
            text.draw()
            return
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.STUDENT_SELECT:
            return
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.PLACING_STUDENT:
            PlacingStudentEvent.drawWidget()
            self.gameReprersentation.afficherTowers()
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            self.gameReprersentation.afficherMobs()
            self.gameReprersentation.afficherTowers()
            self.gameReprersentation.afficherShoots()
            # if len(self.listMobs.listMobsOnMap) == 0 and len(self.mobToSpawn) == 0:
            #     pyglet.clock.unschedule(self.updateGame)
        elif GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAMEOVER:
            self.gameOverBackground.blit(0, 0, 0)
            gameover = pyglet.text.Label("Game Over",
                                   font_name='Times New Roman',
                                   font_size=80,
                                   x=420, y=100,
                                   color=(255, 0, 0, 255),
                                   anchor_x='left', anchor_y='center')
            gameover.draw()
            score = pyglet.text.Label("Score atteint : [" + str(self.gameReprersentation.yearNumber) + " Années] Très Impressionant !",
                                         font_name='Times New Roman',
                                         font_size=20,
                                         x=420, y=40,
                                         color=(0, 0, 0, 255),
                                         anchor_x='left', anchor_y='center')
            score.draw()
            pass


        DisplayCharacteristics.drawDetailObject()

    def InitCustomEventsByGamePhase(self):
        EventManagement.resetCustomEventStack()
        if GamePhaseEvents.getCurrentGamePhase() == GAMEPHASE.GAME:
            for tower in self.gameReprersentation.listTower:
                EventManagement.addEvent(tower)

