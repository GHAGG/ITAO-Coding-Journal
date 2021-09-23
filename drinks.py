class Drink:
    def __init__(self, syrup = "Water", water = "plain", calories = 0, iceratio = 0):
        self.syrup = "water"
        self.water = "plain"
        self._calories = 0
        self.iceratio = 0
    def __repr__(self):
        return self.syrup
    def cal(self):
        return self._calories

class Soda(Drink):
    def __init__(self, syrup = 'none', water = 'carbonated'):
        self.syrup = "none"
        self.water = "carbonated"
        self._calories = 100

class Sprite(Soda):
    def __init__(self, syrup = 'Sprite', water = 'carbonated'):
        self.syrup = "Sprite"
        self.water = "Carbonated"
        self._calories = 100

class DietSprite(Sprite):
    def __init__(self, syrup = 'Sprite', water = 'carbonated'):
        self.syrup = "Sprite"
        self.water = "Carbonated"
        self._calories = 0

class Coke(Soda):
    def __init__(self, syrup = 'Coke', water = 'carbonated'):
        self.syrup = "Coke"
        self.water = "Carbonated"
        self._calories = 100

class DietCoke(Coke):
    def __init__(self, syrup = 'Coke', water = 'carbonated'):
        self.syrup = "Coke"
        self.water = "Carbonated"
        self._calories = 0
