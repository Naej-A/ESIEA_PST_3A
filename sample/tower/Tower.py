import pyglet
import sample.IsometricTools as IsoTools
import sample.gui.DisplayCharacteristics as DisplayCharacteristics
import sample.shoot.Shoot as Shoot
import math
import sample.IsometricTools as IsometricTools

class FieldToEvolveNotFound(Exception):
    "Raised when the fild to evolve is not found"
    pass

class StatToAddNotFound(Exception):
    "Raised when the fild to evolve is not found"
    pass


class Tower(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    dictionaryStuding = {"maths": {"level0": {"price": 30,
                            "stat": 5},
                 "level1": {"price": 40,
                            "stat": 5},
                 "level2": {"price": 90,
                            "stat": 10},
                 "level3": {"price": 120,
                            "stat": 15},
                 "level4": {"price": 250,
                            "stat": 50},
                 "level5": {"price" : "MAX",
                            "stat": 0}
                 },
        "elec": {"level0": {"price": 20,
                            "stat": 0.1},
                 "level1": {"price": 25,
                            "stat": 0.1},
                 "level2": {"price": 70,
                            "stat": 0.3},
                 "level3": {"price": 115,
                            "stat": 0.5},
                 "level4": {"price": 250,
                            "stat": 2},
                 "level5": {"price" : "MAX",
                            "stat": 0}
                 },
        "res": {"level0": {"price": 30,
                           "stat": 10},
                "level1": {"price": 35,
                           "stat": 10},
                "level2": {"price": 100,
                           "stat": 20},
                "level3": {"price": 250,
                           "stat": 40},
                "level4": {"price": 500,
                           "stat": 100},
                 "level5": {"price" : "MAX",
                            "stat": 0}
                },
        "curio": {"level0": {"price": 50,
                          "stat": 5},
               "level1": {"price": 50,
                          "stat": 5},
               "level2": {"price": 50,
                          "stat": 5},
               "level3": {"price": 50,
                          "stat": 5},
               "level4": {"price": 100,
                          "stat": 10},
               "level5": {"price" : "MAX",
                            "stat": 0}
               }}
    def __init__(self, xPixel, yPixel, xBlock, yBlock, name):
        image = open('ressources/ESIEA/ESIEA1A.png', 'rb')  # Lecture du fichier en binaire
        img = pyglet.image.load('ressources/ESIEA/ESIEA1A.png', file=image)
        super().__init__(img, xPixel, yPixel)
        self.scale = 1.7
        self.xBlock = xBlock
        self.yBlock = yBlock
        self.name = name
        self.year = 1
        self.evolutionBlock = Tower.getEvolutionBlock(self.year)
        self.attack = 50
        self.attackSpeed = 0.5 #Nombre de tirs par secondes
        self.attackCooldown = 0
        self.range = 20
        self.curiosity = 0
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
        pathToImage = \
            "ressources/ESIEA/ESIEA" + str(self.year) + "A.png"
        image = open(pathToImage, 'rb')  # Lecture du fichier en binaire
        self.image = pyglet.image.load(pathToImage, file=image)
        self.evolutionBlock = Tower.getEvolutionBlock(self.year)

    def upgradeEducationField(self, educationnalField):
        if educationnalField.level < educationnalField.maxLevel:
            if educationnalField.name == "math":
                self.attackPower += educationnalField.intToAddToStat
                educationnalField.level += 1

    @staticmethod
    def getEvolutionBlock(year):

        return Tower.createEducationBlock1A()


    @staticmethod
    def createEducationBlock1A():
        listField = list()
        listField.append(educationField(None, "computerScience", 5, Tower.dictionaryStuding["maths"], "attack"))
        listField.append(educationField(None, "livingLanguage", 5, Tower.dictionaryStuding["elec"], "attackSpeed"))
        listField.append(educationField(None, "electronics", 5, Tower.dictionaryStuding["res"], "range"))
        listField.append(educationField(None, "projectManagement", 5, Tower.dictionaryStuding["curio"], "curiosity"))
        return listField

    @staticmethod
    def createEducationBlock2A():
        listField = list()
        listField.append(educationField(None, "computerScience", 5, Tower.dictionaryStuding["maths"], "attack"))
        listField.append(educationField(None, "livingLanguage", 5, Tower.dictionaryStuding["elec"], "attackSpeed"))
        listField.append(educationField(None, "electronics", 5, Tower.dictionaryStuding["res"], "range"))
        listField.append(educationField(None, "projectManagement", 5, Tower.dictionaryStuding["curio"], "curiosity"))
        return listField

    @staticmethod
    def createEducationBlock3A():
        listField = list()
        listField.append(educationField(None, "computerScience", 5, Tower.dictionaryStuding["maths"], "attack"))
        listField.append(educationField(None, "livingLanguage", 5, Tower.dictionaryStuding["elec"], "attackSpeed"))
        listField.append(educationField(None, "electronics", 5, Tower.dictionaryStuding["res"], "range"))
        listField.append(educationField(None, "projectManagement", 5, Tower.dictionaryStuding["curio"], "curiosity"))
        return listField

    def increaseLevelEducationField(self, educationFieldToSearch):
        compteur = 0
        print(educationFieldToSearch)
        for tempEducationField in self.evolutionBlock:
            if tempEducationField == educationFieldToSearch:
                if not tempEducationField.nextEvolution: # si la prochaine évolution est vide (none)
                    return tempEducationField
                tempEducationField = tempEducationField.nextEvolution
                self.evolutionBlock[compteur] = tempEducationField
                if tempEducationField.nameStatToAdd == "attack":
                    self.attack += tempEducationField.intToAddToStat
                    return tempEducationField
                if tempEducationField.nameStatToAdd == "attackSpeed":
                    self.attackSpeed += tempEducationField.intToAddToStat
                    return tempEducationField
                if tempEducationField.nameStatToAdd == "range":
                    self.range += tempEducationField.intToAddToStat
                    return tempEducationField
                if tempEducationField.nameStatToAdd == "curiosity":
                    self.attack += tempEducationField.intToAddToStat
                    return tempEducationField
                raise StatToAddNotFound
            compteur += 1
        print(educationFieldToSearch)
        raise FieldToEvolveNotFound

    def shooting(self, gameProgress):
        ListMob = gameProgress.listMobs.listMobsOnMap
        ListShoot = gameProgress.listShoot
        farrestMobInRange = None
        for mob in ListMob:
            if math.sqrt(pow(mob.xBlock - self.xBlock, 2) + pow(mob.yBlock - self.yBlock, 2)) <= self.range: #Est-ce que le mob est dans la range de la tour
                if farrestMobInRange != None:
                    if mob.idZone >= farrestMobInRange.idZone:
                        if math.sqrt(pow(mob.xBlock - mob.destinationX, 2) + pow(mob.yBlock - mob.destinationY, 2)) < math.sqrt(pow(farrestMobInRange.xBlock - farrestMobInRange.destinationX, 2) + pow(farrestMobInRange.yBlock - farrestMobInRange.destinationY, 2)): #Est-ce le mob est plus proche de la fin que le farrestMobInRange
                            farrestMobInRange = mob
                else:
                    farrestMobInRange = mob
        if farrestMobInRange != None:
            shoot = Shoot.Shoot(0, 0, self.xBlock - 10, self.yBlock - 10, farrestMobInRange, 2, self.attack) #Vitesse du projectile à gérer, pour l'instant à 2
            ListShoot.append(shoot)
            if farrestMobInRange.yBlock - farrestMobInRange.xBlock < self.yBlock - self.xBlock:
                self.scale_x = 1
            else:
                self.scale_x = -1
            self.updatePixelCoordinates(gameProgress)

            return True
        return False

    def updatePixelCoordinates(self, gameProgress):
        self.x, self.y = IsometricTools.coordinateToPixel(gameProgress, self.xBlock, self.yBlock)
        self.x -= self.width * self.scale_x / 2

    def __str__(self):
        return "[name :" + self.name +  \
               " | year : " + str(self.year) + \
               " | attack : " + str(self.attack) + \
               " | attackSpeed : " + str(self.attackSpeed) + \
               " | range :" + str(self.range) + \
               " | curiosity : " + str(self.curiosity) + \
               " | description : " + str(self.description) + \
                "]"

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
        if (x >= self.x and x < self.x + self.width and y >= self.y and y < self.y + self.height):
            # Dispatch the custom event
            self.displayCharacteristics.dispatch_event('on_clickShowCharacteristique', self)
            return True
        else:
            self.displayCharacteristics.dispatch_event('on_clickUnShowCharacteristique', x, y)
            pass




class educationField:
    def __init__(self, precedentEvolution, name, maxLevel, dictionary, nameStatToAdd):
        self.precedentEvolution = precedentEvolution
        if not self.precedentEvolution:
            self.level = 0
        else:
            self.level = self.precedentEvolution.level + 1
        self.nextEvolution = None
        self.name = name
        self.maxLevel = maxLevel
        self.price = dictionary["level" + str(self.level)]["price"]
        self.intToAddToStat = dictionary["level" + str(self.level)]["stat"]
        self.nameStatToAdd = nameStatToAdd
        self.isBuyable = False
        self.currentLevel = 0
        self._initTreeToMaxLevel(dictionary)



    def _initTreeToMaxLevel(self, dictionary):
        """
        init the tree of evolution
        :param basePrice: le prix minimum auquel
        :param baseIntToAddToStat: the minimum int stat
        :return: an education field instance
        """

        if self.level >= self.maxLevel:
            return None
        if self.level < self.maxLevel:
            self.nextEvolution = educationField(self, self.name, self.maxLevel, dictionary, self.nameStatToAdd)
        self.nextEvolution._initTreeToMaxLevel(dictionary)
        return self

    def __str__(self):
        return "Education Field[" \
               "level :"+ str(self.level)+"|" \
               "name :"+ str(self.name )+"|" \
               "prix :"+ str(self.price )+"|" \
               "nom stat :"+ str(self.nameStatToAdd )+"]"