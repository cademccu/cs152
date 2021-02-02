def writeToFile(string, filename):
    with open(filename, 'w') as f:
        f.write(string)


def printFile(filename):
    with open(filename, 'r') as f:
        print(f.read())

def writeListToFile(l, filename):
    with open(filename, 'a') as f:
        for s in l:
            f.write(str(s) + "\n")
        

    
def writeUserInfo(name, password, filename):
    with open(filename, 'a') as f:
        f.write("name=" + name + "\n")
        f.write("password=" + password + "\n")
    
def sumFile(filename):
    total = 0.0
    with open(filename, 'r') as f:
        for n in f.readlines():
            total += float(n)
    return total
    
def nameInFile(user, filename):
    with open(filename, 'r') as f:
        for s in f.readlines():
            if user in s:
                return True
    return False

def main():
    writeToFile("Hello, World\n", "hello.txt")
    printFile("hello.txt") 
    writeListToFile([1,2,3,4], "myfile.txt")
    printFile("myfile.txt") 
    writeUserInfo("casey","walrus7","secret_file")
    writeUserInfo("riley","python_is_fun","secret_file")
    printFile("secret_file")
    print(sumFile("myfile.txt"))
    print(nameInFile('casey', 'secret_file'))
    
if __name__ == '__main__':
    main()
