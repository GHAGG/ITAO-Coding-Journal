from mod.drinks import *

drinktypes = ["Sprite", "Water", "Coke"]
allcal = []

drink = input("Which drink would you like today? ")
try:
    drink = str(drink)
except:
    "Invalid Input"
else:
    if "Diet" in drink.split().capitalize:
        pass
    drink = drink.capitalize()
    if drink in drinktypes:
        if (drink == "Sprite"):
            drink = Sprite()
        elif (drink == "Coke"):
            drink = Coke()
        elif (drink == "Water"):
            drink = Drink()
        print("A {} has {} calories".format(drink.syrup, drink.cal()))
        allcal.append(drink.cal())