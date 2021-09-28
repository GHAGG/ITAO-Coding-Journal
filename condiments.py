class Condiment():
    def __init__(self, condimenttype, calories = 20):
        self.condimenttype = condimenttype
        self._calories = 20
    def __repr__(self):
        return self.condimenttype
    def cal(self):
        return self._calories

class Sauce():
    def __init__(self, saucetype, calories = 20):
        self.saucetype = saucetype
        self._calories = 20
    def __repr__(self):
        return self.saucetype
    def cal(self):
        return self._calories