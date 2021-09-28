from mod.drinks import *
from mod.entree import *
from mod.condiments import *
alldrinktypes = ["Sprite", "Diet Sprite", "Coke", "Diet Coke", "Water"]
drinktypes = ["Sprite", "Water", "Coke"]
entreetypes = ["Burger", "Nuggets"]
condimenttypes = ["Ketchup", "Extra Cheese", "Caramelized Onions", "Onions", "Mustard", "Mayonnaise", "Mayo", "Pickles"]
YN = ["Y", "N"]
drinksordered = []
allcal = []
entreeordered = []
condimentsordered = []

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%% H A P P Y  M E A L %%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

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
            drinksordered.append(drink)
        elif drink in drinktypes:
            if (drink == "Sprite"):
                drink = Sprite()
            elif (drink == "Coke"):
                drink = Coke()
            elif (drink == "Water"):
                drink = Drink()
            print("A {} has {} calories".format(drink.syrup, drink.cal()))
            allcal.append(drink.cal())
            drinksordered.append(drink)
        elif drink not in drinktypes:
            print("The drink you ordered is not in our menu, please order a different drink")
            continue

        while True:
            another = str(input("Would you like to order another drink? (Y/N) "))
            if another.capitalize() in YN:
                break
            else:
                print("Please enter 'Y' or 'N' as a response")
        if (another.capitalize() == 'Y'):
            continue
        else:
            break

while True:
    entree = str(input("Would you like your meal to come with a burger or nuggets: ")).capitalize()
    if entree in entreetypes:
        if entree == "Burger":
            entree = Burger()
            entreeordered.append(entree)
            allcal.append(entree.cal())
            times = 0
            while times < 1:
                condimentsyesno = str(input("Would you like any condiments on your burger? (Y/N) ")).capitalize()
                if condimentsyesno in YN:
                    times += 1
                else:
                    print("Please enter 'Y' or 'N' as a response")
            if (condimentsyesno == 'Y'):
                while True:
                    try:
                        howmanycondiments = int(input("How many condiments would you like on your burger? (int) "))
                    except:
                        print("Invalid input. Please enter a whole number")
                        continue
                    else:
                        i = 0
                        while i < howmanycondiments:
                            i += 1
                            while True:
                                whichcondiment = str(input("Which condiment would you like on your burger? (please enter only one condiment at a time) ")).capitalize()
                                if whichcondiment in condimenttypes:
                                    break
                                else:
                                    seecondiments = str(input("We do not have that condiment on our menu. Would you like to see our condiment menu before you input another condiment? ")).capitalize()
                                    if seecondiments == "Y":
                                        print(condimenttypes)
                                        continue
                                    else:
                                        continue
                            condiment = Condiment(condimenttype = whichcondiment)
                            condimentsordered.append(condiment)
                            allcal.append(condiment.cal())
                    break
                print("A {} with {} has been added to your order". format(entree, condimentsordered))
                break
            else:
                break
        break
    else:
        print("The entree you ordered is not on our menu, please order a different entree")
        continue

totalcalories = sum(allcal)
print("So far, your order has {} calories".format(totalcalories))