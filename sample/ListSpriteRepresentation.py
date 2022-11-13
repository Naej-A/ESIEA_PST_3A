import SpriteRepresentation as sr
from enum import Enum

# class syntax
class SpriteEnum(Enum):
    Mini_block_rouge = 1

class ListSpriteRepresentation:
    enumObjet = Enum('Color', ['RED', 'GREEN', 'BLUE'])
    def __init__(self):
        self.listSprite = list()
        self._init_All_Sprite()

    def _init_All_Sprite(self):
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Mini_block_rouge.png"))
        return 0

    def findSpriteByImageName(self, name):
        for sprite in self.listSprite:
            if sprite.imageName == name:
                return sprite
        return None

    def findSpriteById(self, idSprite):
        return self.listSprite[idSprite]