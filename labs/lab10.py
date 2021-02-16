def readLettersFromFile(filename):
    """ Return all characters from file in a list"""
    chars = []
    with open(filename) as f:
        l = f.readlines()
        for line in l:
            chars.extend(line.split())
    return chars

def countLetters(lettersFromFile):
    """Return dictionary of key:value pairs (letter,# times letter appears in file)"""
    mydict = {}
    for letter in lettersFromFile:
        if letter in mydict:
            mydict[letter] += 1
        else:
            mydict[letter] = 1
    return mydict

def keyyy(s):
    # idk if im allowed to use lambdas sooooo
    return s[0], s[1]
    
def sortByCount(count):
    """Return list of tuples (value,key), sorted by value"""
    l = list(count.items())
    # dirty but whateva
    ll = []
    for tup in l:
        temp = (tup[1], tup[0])
        ll.append(temp)

    return sorted(ll, key = keyyy)
        
def main():
    """DO NOT CHANGE THIS"""
    filename = input("filename?\n")
    letters = readLettersFromFile(filename)
    print("Letters:", letters)
    
    count = countLetters(letters)
    print("Counted Letters", count)
    
    countSorted = sortByCount(count)
    print("Sorted:", countSorted)

if __name__ == "__main__":
    main()
