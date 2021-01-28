def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        return 0
    else: 
        return n * factorial(n - 1) 

def fib(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def exponent(n):
    if n == 0: 
        return 1
    elif n < 0: 
        return 0
    else:
        return 2 * exponent(n-1)

def main():
    print(factorial(5))
    print(exponent(4))
    print(fib(7))
    
if __name__ == "__main__":
    main()
