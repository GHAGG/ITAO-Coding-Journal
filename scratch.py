from mod.drinks import *

drinktypes = ["Sprite", "Water", "Coke"]
YN = ["Y", "N"]
drinksordered = []
allcal = []


while True:
    try:
        drink = str(input("Which drink would you like today? "))
    except:
        "Invalid Input"
    else:
        drink = drink.capitalize()
        if "Diet" in drink.split():
            if (drink == "Diet Coke"):
                drink = DietCoke()
            elif (drink == "Diet Sprite"):
                drink = DietSprite()
            print("A {} has 0 calories".format(drink))
            allcal.append(0)
            drinktypes.append(drink)
        elif drink in drinktypes:
            if (drink == "Sprite"):
                drink = Sprite()
            elif (drink == "Coke"):
                drink = Coke()
            elif (drink == "Water"):
                drink = Drink()
            print("A {} has {} calories".format(drink.syrup, drink.cal()))
            allcal.append(drink.cal())
            drinktypes.append(drink.syrup)
        another = str(input("Would you like to order another drink? (Y/N) "))
        try:
            another.capitalize() in YN
        except:
            print("Please enter 'Y' or 'N' as a response")
        else:
            another.capitalize()
            if (another.capitalize() == 'Y'):
                continue
            else:
                break