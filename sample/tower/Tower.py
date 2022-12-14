import pyglet
class Tower(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, img, x, y, name):
        super().__init__(img, x, y)
        self.x = x
        self.y = y
        self.name = name
        self.year = 1
        self.evolutionBlock = Tower.getEvolutionBlock(self.year)
        self.attackPower = 0
        self.reloadSpeed = 0
        self.shootRadius = 0
        self.description = ""
        self.major = None
        #plus tard on peut avoir des sous classe d'étudiant qui représente les natures

    def studentCanPassNextYear(self):
        """
        check if a student can pass next year
        :return: true if student has at least 8/20 in total
        """
        max = 0
        current = 0
        for field in self.evolutionBlock:
            max += field.maxLevel
            current += field.currentLevel
        return current / max > 0.4

    def studentPassNextYear(self):
        self.year += 1
        self.evolutionBlock = Tower.getEvolutionBlock(self.year)

    def upgradeEducationField(self, educationnalField):
        if educationnalField.level < educationnalField.maxLevel:
            if educationnalField.name == "math":
                self.attackPower += educationnalField.intToAddToStat
                educationnalField.level+= 1

    @staticmethod
    def getEvolutionBlock(year):
        if year == 1:
            return Tower.createEducationBlock1A()
        elif year == 2:
            return Tower.createEducationBlock2A()
        elif year == 3:
            return Tower.createEducationBlock3A()
        return -1

    @staticmethod
    def createEducationBlock1A():
        listField =  list()
        return listField

    @staticmethod
    def createEducationBlock2A():
        listField =  list()
        return listField

    @staticmethod
    def createEducationBlock3A():
        listField =  list()
        return listField

# ===== fonction graphique =======
    def on_mouse_motion(self, x, y, dx, dy):
        if (x >= self.x and x < self.x + self.width and y >= self.y and y < self.y + self.height):
            pass

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if the mouse click occurred inside the sprite
        if (x >= self.x and x < self.x + self.width and
            y >= self.y and y < self.y + self.height):
            # Dispatch the custom event
            print(self.name)
            #self.dispatch_event('on_clank')
            return True



class educationField:
    def __init__(self, father, name, maxLevel, basePrice, intToAddToStat, year):
        self.father = father
        self.name = name
        self.children = list()
        self.isBuyable = False
        self.maxLevel = maxLevel
        self.currentLevel = 0
        self.basePrice = basePrice
        self.intToAddToStat = intToAddToStat
        self.year = year
