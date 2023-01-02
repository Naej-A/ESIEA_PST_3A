import sample.shoot.Shoot

class ShootExplosive(sample.shoot.Shoot):

    def __init__(self, range, mobTarget, speed, damage, x, y):
        super.__init__(mobTarget, speed, damage, x, y)
        self.range = range

    def onHitEffect(self):
        # Trouver un moyen de faire passer la liste de mob ici
        return None