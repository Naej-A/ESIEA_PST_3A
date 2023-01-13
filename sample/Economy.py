
class Economy():
    estacaTears = 300

    @staticmethod
    def buy(price):
        if Economy.estacaTears >= price:
            Economy.estacaTears -= price
            return True
        else:
            return False