planets = {}

def processLine(line):
    s = line.split(",")
    planets[s[0]] = float(s[1])

def processFile(filename):
    with open(filename, "r") as f:
        f.readline() # burn header
        while True:
            line = f.readline()
            if not line:
                break;
            else:
                processLine(line)

def getPlanets():
    return planets
