class Drink:
    def __init__(self):
        self.syrup = "Water"
        self.water = "plain"
        self._calories = 0
        self.iceratio = 0
    def __repr__(self):
        return self.syrup

    def calories(self):
        return self._calories()


class Soda(Drink):
    def __init__(self, syrup = 'none', water = 'carbonated'):
        self.syrup = syrup
        self.water = water
        self._calories = 100

class Sprite(Soda):
    def __init__(self):
        super().__init__('Sprite')

#DrinkSelect = input("Please select a drink for your happy meal")

#DrinkSelect

#try:
    #DrinkSelect = str(DrinkSelect)
#except:
    #print("Invalid input, please enter a valid drink name")
#else:

