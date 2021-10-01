toytypes = ["Pokemon cards", "Star wars toy", "Princess toy", "Car toy", "Plush toy"]

class Toy():
    def __init__(self, keynum):
        from scratch import toydict
        self.toyval = toydict[keynum]

    def __repr__(self):
        return self.toyval
