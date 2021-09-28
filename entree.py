class Burger():
    def __init__(self, dish = 'Burger', calories = 300, addcondiments = True):
        self.dish = 'Burger'
        self._calories = 300
        self.addcondiments = addcondiments
    def __repr__(self):
        return self.dish
    def cal(self):
        return self._calories

class Nuggets():
    def __init__(self, dish = 'Nuggets', calories = 200, addsauce = True):
        self.dish = 'Nuggets'
        self._calories = 200
        self.addsauce = addsauce
    def __repr__(self):
        return self.dish
    def cal(self):
        return self._calories