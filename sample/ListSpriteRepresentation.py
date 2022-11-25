import sample.SpriteRepresentation as sr
from enum import Enum

# class syntax

class ListSpriteRepresentation:
    def __init__(self):
        self.listSprite = list()
        self._init_All_Sprite()

    def _init_All_Sprite(self):
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Mini_block_bleu.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Mini_block_jaune.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Mini_block_rouge.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Mini_block_vert.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1]], "Colone_rouge.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 2, [[-1, -1, -1],
                                                              [-1, -1, -1],
                                                              [-1, -1, -1]], "Platforme.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 2, [[-1, -1, -1],
                                                              [-1, -1, -1],
                                                              [-1, -1, -1]], "Block_bleu.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 2, [[-1, -1, -1],
                                                              [-1, -1, -1],
                                                              [-1, -1, -1]], "Block_jaune.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 2, [[-1, -1, -1],
                                                              [-1, -1, -1],
                                                              [-1, -1, -1]], "Block_rouge.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 2, [[-1, -1, -1],
                                                              [-1, -1, -1],
                                                              [-1, -1, -1]], "Block_vert.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 20, [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]], "Giga_block_gris.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1]], "Gros_block_bleu.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1]], "Gros_block_jaune.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1]], "Gros_block_rouge.png"))
        self.listSprite.append(sr.SpriteRepresentation(0, 0, [[-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1],
                                                              [-1, -1, -1, -1, -1]], "Gros_block_vert.png"))

        return 0

    def findSpriteByImageName(self, name):
        for sprite in self.listSprite:
            if sprite.imageName == name:
                return sprite
        return None

    def findSpriteById(self, idSprite):
        for sprite in self.listSprite:
            if sprite.id == idSprite:
                return sprite
        return None

