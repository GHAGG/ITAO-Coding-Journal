class Fries():
    def __init__(self, name = "Fries", calories = 150, sodium = 20):
        self.name = "Fries"
        self._calories = 150
        self.sodium = 20

    def __repr__(self):
        return self.name

    def cal(self):
        return self._calories

class SmallFries(Fries):
    def __init__(self, name="Fries", calories=150, sodium=20):
        self.name = "Fries"
        self._calories = 100
        self.sodium = 15

class LargeFries(Fries):
    def __init__(self, name="Fries", calories=150, sodium=20):
        self.name = "Fries"
        self._calories = 200
        self.sodium = 25

class AppleSlices():
    def __init__(self, name = "Apple Slices", calories = 50):
        self.name = "Apple Slices"
        self._calories = 50

    def __repr__(self):
        return self.name

    def cal(self):
        return self._calories