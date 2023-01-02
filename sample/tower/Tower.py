import pyglet
import sample.IsometricTools as IsoTools
import sample.gui.DisplayCharacteristics as DisplayCharacteristics

class Tower(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, img, xPixel, yPixel, xBlock, yBlock, name):
        super().__init__(img, xPixel, yPixel)
        self.xBlock = xBlock
        self.yBlock = yBlock
        self.name = name
        self.year = 1
        self.evolutionBlock = Tower.getEvolutionBlock(self.year)
        self.attackPower = 0
        self.reloadSpeed = 0
        self.shootRadius = 0
        self.description = ""
        self.major = None
        self.displayCharacteristics = DisplayCharacteristics.DisplayCharacteristics()
        self.isDetailsShown = False
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
        listField = list()
        listField.append(educationField(None, "computerScience", 5, 10, 3, "attack"))
        listField.append(educationField(None, "livingLanguage", 5, 10, 3, "slowing"))
        listField.append(educationField(None, "electronics", 5, 10, 3, "reload"))
        listField.append(educationField(None, "projectManagement", 5, 10, 3, "alliesIncrease"))
        return listField

    @staticmethod
    def createEducationBlock2A():
        listField = list()
        listField.append(educationField(None, "2A_1", 5, 10, 3, "attack"))
        listField.append(educationField(None, "2A_2", 5, 10, 3, "slowing"))
        listField.append(educationField(None, "2A_3", 5, 10, 3, "reload"))
        listField.append(educationField(None, "2A_4", 5, 10, 3, "alliesIncrease"))
        return listField

    @staticmethod
    def createEducationBlock3A():
        listField = list()
        listField.append(educationField(None, "3A_1", 5, 10, 3, "attack"))
        listField.append(educationField(None, "3A_2", 5, 10, 3, "slowing"))
        listField.append(educationField(None, "3A_3", 5, 10, 3, "reload"))
        listField.append(educationField(None, "3A_4", 5, 10, 3, "alliesIncrease"))
        return listField

# ===== fonction graphique =======
    def on_mouse_motion(self, x, y, dx, dy):
        if (x >= self.x and x < self.x + self.width and y >= self.y and y < self.y + self.height):
            self.displayCharacteristics.dispatch_event('on_showCharacteristique', self)
            self.isDetailsShown = True
            return
        elif self.isDetailsShown:
            self.isDetailsShown = False
            self.displayCharacteristics.dispatch_event("on_unShowCharacteristique")
            pass

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if the mouse click occurred inside the sprite
        if (x >= self.x and x < self.x + self.width and
            y >= self.y and y < self.y + self.height):
            # Dispatch the custom event
            print(self.name)
            self.displayCharacteristics.characteristique(self)
            return True



class educationField:
    def __init__(self, precedentEvolution, name, maxLevel, price, intToAddToStat, nameStatToAdd):
        self.precedentEvolution = precedentEvolution
        self.nextEvolution = None
        self.name = name
        self.maxLevel = maxLevel
        self.price = price
        self.intToAddToStat = intToAddToStat
        self.nameStatToAdd = nameStatToAdd
        self.isBuyable = False
        self.currentLevel = 0
        self.level = 0
        self._initTreeToMaxLevel(price, intToAddToStat)

    def _initTreeToMaxLevel(self, basePrice, baseIntToAddToStat):
        """
        init the tree of evolution
        :param basePrice: le prix minimum auquel
        :param baseIntToAddToStat: the minimum int stat
        :return: an education field instance
        """
        if not self.precedentEvolution :
            self.level = 0
        else:
            self.level = self.precedentEvolution.level + 1

        if self.level >= self.maxLevel:
            return None

        self.nextEvolution = educationField(self, self.name, self.maxLevel, basePrice * self.level,
                                            self.intToAddToStat * self.level, self.nameStatToAdd)
        self.nextEvolution._initTreeToMaxLevel(basePrice, baseIntToAddToStat)
        return self