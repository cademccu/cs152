favoriteSeason = ""

def getInput():
    color = input("Input a color\n")
    number1 = input("Input a number\n")
    number2 = input("Input a second number\n")
    season_local = input("Input a season\n")

    return color, number1, number2, season_local

def printColor(color):
    print("Favorite color is {}".format(color))
    return

def addNumbers(a, b):
    return a + b

def setGlobal(season):
    global favoriteSeason
    favoriteSeason = season
    return

def main():
    color, number1, number2, season_local = getInput()
    printColor(color)
    addNumbers(number1, number2)
    setGlobal(season_local)

if __name__ == '__main__':
	main()
