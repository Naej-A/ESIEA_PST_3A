#TODO: faire les fonctions rotation horaire et rotation antihoraire
#TODO: faire un affichage de debug correcte car pour l'instant cela marche uniquement avec les maps carré
#TODO: fonction ajoute spriteRepresentation à representationCarte
import sample.ListSpriteRepresentation as lsp
import numpy as np
class MapRepresentation:
    ratioPixel = 15

    def __init__(self, absysseX, ordonneeY):
        self.absysseX = absysseX
        self.ordonneeY = ordonneeY
        self._init_carte()
        self.positionCamera = 0 # 0 = 0° | 1 = 90° | 2 = 180° | 3 = 270°
        self.listSpriteRepresentation = lsp.ListSpriteRepresentation()


    def _init_carte(self):
        self.representationCarte = []
        for k in range(self.absysseX * self.ordonneeY):
            self.representationCarte.append(0)
        return 0

    # ne marche pas encore il faut choper l'index Y et X pour l'affichage
    def afficheCarteCarreDebug(self):
        tailleAAfficher = self.absysseX + self.absysseX - 1
        vide = "R=_|"
        vide = "   |"
        for i in range(tailleAAfficher):
            print("|", end="")
            nbCaseVide = abs(tailleAAfficher//2 - i)
            for numVide in range (nbCaseVide):
                print(vide, end="")
            for indexLigneCaseRepresente in range(tailleAAfficher - (2* nbCaseVide) - (tailleAAfficher - (2* nbCaseVide))//2 ):
                index = 0
                if indexLigneCaseRepresente != 0:
                    print(vide, end="")
                print("R="+str(self.representationCarte[0])
                      +"|" , end="")
            for numVide in range (nbCaseVide):
                print(vide, end="")
            print() #newline
        return 0

    def traductionRotation90Antihoraire(self):
        self.positionCamera = self.positionCamera - 1 % 4
        # ------ code pour changer la carte vers -90 -----
        return 0

    def traductionRotation90HoraireV1(self):
        self.positionCamera = self.positionCamera + 1 % 4
        # ------ code pour changer la carte vers +90 -----
        temp = ()
        for x in range(0, self.absysseX):
            for y in range(self.ordonneeY-1, 0-1, -1):
                temp.append(self.representationCarte[y*self.ordonneeY + x])
        self.representationCarte = temp
        return 0

    def ajouteSpriteToMap(self):
        #il manque encore la fonction
        return 0