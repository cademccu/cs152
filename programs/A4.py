# Unit conversions

recipe = 'Lemonade'
units = ''

def convertIngredients(lemon, water, sugar, servings, newServings):
	# return the amount of each ingredient required for the new serving size
    ratio = newServings/servings
    return lemon * ratio, water * ratio, sugar * ratio, newServings

def getIngredients():
	# obtain input for each of the ingredients
	# obtain input for how many servings these ingredients would make
    lemon = input("Enter amount of lemon juice in cup(s)?\n")
    water = input("Enter amount of water in cup(s)?\n")
    agave = input("Enter amount of agave nectar in cup(s)?\n")
    servings = input("How many servings of Lemonade does this make?\n")
    return float(lemon), float(water), float(agave), float(servings)

def printIngredients(lemon, water, sugar, servings):
	# print the ingredients required for an amount of servings
    global recipe, units

    print(recipe + " ingredients for %.1f servings" % float(servings))
    print("%.1f cup(s) lemon juice" % float(lemon))
    print("%.1f cup(s) water" % float(water))
    print("%.1f cup(s) agave nectar" % float(sugar))
    


def main():
	# convert a recipe to a different number of servings
	global units
	units = input('What is the unit of measure?\n')
	lemon, water, sugar, servings = getIngredients()
	printIngredients(lemon, water, sugar, servings)
	newServings = float(input('How many servings would you like to make?\n'))
	lemon, water, sugar, servings = convertIngredients(lemon, water, sugar, servings, newServings)
	printIngredients(lemon, water, sugar, servings)


if __name__ == '__main__':
	main()
