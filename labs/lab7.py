def countDown(first, last):
    while first >= last:
        print(str(first), end=" ")
        first -= 1
    print()

def oddNumbers(N):
    i = 1
    x = []
    for i in range(N + 1):
        if (i) % 2 == 1:
            x.append(i)
    return x


def reverse(s):
    return "".join(reversed(s)) # lol gonna start using threads on god

def countInput():
    s = input()
    count = 1
    while s != "stop":
        s = input()
        count += 1
        
    return count

# Write some tests here to see if your code works
def main():
    oddNumbers(99)

# Do not modify the code below
if __name__ == '__main__':
    main()
