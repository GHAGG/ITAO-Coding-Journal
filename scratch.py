from mod.drinks import *
from mod.entree import *
from mod.condiments import *
from mod.sides import *
from mod.toy import *

import random as r

alldrinktypes = ["Sprite", "Diet Sprite", "Coke", "Diet Coke", "Water"]
drinktypes = ["Sprite", "Water", "Coke"]
entreetypes = ["Burger", "Nuggets"]
condimenttypes = ["Ketchup", "Extra cheese", "Caramelized onions", "Onions", "Mustard", "Mayonnaise", "Mayo", "Pickles"]
saucetypes = ["Ketchup", "Bbq", "Honey mustard", "Mustard", "Ranch"]
sidetypes = ["Fries", "Apple slices", "Apples"]
frytypes = ["Small", "Medium", "Large"]
toytypes = ["Pokemon cards", "Star wars toy", "Princess toy", "Car toy", "Plush toy"]
#toydict = {1:"Pokemon cards", 2:"Star wars toy", 3:"Princess toy", 4:"Car toy", 5:"Plush toy"}
YN = ["Y", "N"]
drinksordered = []
allcal = []
entreeordered = []
condimentsordered = []
sideordered = []
toyordered = []

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
            break
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
            break
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
        if entree == "Nuggets":
            entree = Nuggets()
            entreeordered.append(entree)
            allcal.append(entree.cal())
            times = 0
            while True:
                sauceyesno = str(input("Would you like any sauce for your nuggets? (Y/N) ")).capitalize()
                if sauceyesno in YN:
                    break
                else:
                    print("Please enter 'Y' or 'N' as a response")
                    continue
            if (sauceyesno == 'Y'):
                while True:
                    whichsauce = str(input("Which sauce would you like to add to your order? ")).capitalize()
                    if whichsauce in saucetypes:
                        sauce = Sauce(saucetype=whichsauce)
                        break
                    else:
                        while True:
                            seesaucesyesno = str(input("That sauce is not available. Would you like to see our sauce menu before selecting another sauce? (Y/N) ")).capitalize()
                            if seesaucesyesno in YN:
                                break
                            else:
                                print("Please enter 'Y' or 'N' as a response")
                                continue
                        if seesaucesyesno == "Y":
                            print(saucetypes)
                            continue
                        else:
                            continue
                allcal.append(sauce.cal())
                print("An entree of {} with {} sauce has been added to your order".format(entree, sauce))
                break
            else:
                print("An entree of {} with no sauce has been added to your order".format(entree))
                break

        elif entree == "Burger":
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

while True:
    sides = str(input("Would you like to order any sides with your happy meal? (Y/N) ")).capitalize()
    if sides in YN:
        break
    else:
        print("Please enter 'Y' or 'N' as a response.")
        continue
if sides == "Y":
    while True:
        sidechoice = str(input("Which side would you like to order, apple slices or fries? ")).capitalize()
        if sidechoice in sidetypes:
            break
        else:
            print("Please enter 'Fries' or 'Apple Slices' as a response.")
    if sidechoice == "Fries":
        while True:
            frysize = str(input("What size fries would you like? ")).capitalize()
            if frysize in frytypes:
                break
            else:
                print("Please enter 'Small', 'Medium', or 'Large' as a response.")
                continue
        if frysize == "Small":
            sideorder = SmallFries()
        elif frysize == "Large":
            sideorder = LargeFries()
        elif frysize == "Large":
            sideorder = Fries()
    elif sidechoice == "Apple slices":
        sideorder = AppleSlices()
    print("A side of {} has been added to your order".format(sideorder))
    sideordered.append(sideorder)
    allcal.append(sideorder.cal())

while True:
    toysee = str(input("Your happy meal comes with a toy, would you like to see which toys we have available? (Y/N) ")).capitalize()
    if toysee in YN:
        break
    else:
        print("Please enter 'Y' or 'N' as a response.")
        continue
if toysee == "Y":
    blank = Toy(keynum = 1)
    print(blank.toydict)
while True:
    care = str(input("Do you care which toy gets added to your meal? (Y/N) ")).capitalize()
    if care in YN:
        break
    else:
        print("Please enter 'Y' or 'N' as a response")
        continue
if care == "Y":
    while True:
        print("As a reminder, your toy options are as follows: ")
        print(blank.toydict)
        toychoice = int(input("Please select the integer corresponding to the toy you want. (int) "))
        #try:
        #    toychoice = int(toychoice)
        #except:
        #    print("Please enter an integer as a response")
        #    continue
        #else:
        #    if toychoice not in range(1,len(toytypes)):
        #        print("Please select an integer from 1 to 5")
        #        continue
        #else:
        toy = Toy(keynum = toychoice)
        toyordered.append(toy)
        print("{} has been added to your Happy Meal".format(toy.toyval))
        break
elif care == "N":
    toychoice = r.randint(1, len(toytypes))
    toy = Toy(keynum=toychoice)
    toyordered.append(toy)
    print("{} has been added to your Happy Meal".format(toy.toyval))


allcalories = sum(allcal)
print("Your order has a total of {} calories".format(allcalories))

while True:
    see = input("Would you like to see a breakdown of your order? (Y/N) ").capitalize()
    if see in YN:
        break
    else:
        print("Please enter 'Y' or 'N' as a response")
        continue
if see == "N":
    print("Your order is being made, have a nice day!")
else:
    if "Burger" in entreeordered:
        if len(condimentsordered) == 0:
            if len(sideordered) == 0:
                print("Today you ordered {} to drink, chose an entree of {} with no condiments, no sides, and (a) {}".format(drinksordered, entreeordered, toyordered))
            else:
                print("Today you ordered {} to drink, chose an entree of {} with no condiments, a side of {}, and (a) {}".format(drinksordered, entreeordered, sideordered, toyordered))
        else:
            if len(sideordered) == 0:
                print("Today you ordered {} to drink, chose an entree of {} with {}, no sides, and (a) {}".format(drinksordered, entreeordered, condimentsordered, toyordered))
            else:
                print(
                    "Today you ordered {} to drink, chose an entree of {} with {}, a side of {}, and (a) {}".format(drinksordered, entreeordered, condimentsordered, sideordered, toyordered))
    else:
        if len(sideordered) == 0:
            print("Today you ordered {} to drink, chose an entree of {}, no sides, and (a) {}".format(drinksordered, entreeordered, toyordered))
        else:
            print("Today you ordered {} to drink, chose an entree of {}, a side of {}, and (a) {}".format(drinksordered, entreeordered, sideordered, toyordered))

print("Goodbye!")
