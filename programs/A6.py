# Is some text a palindrome?

def palindrome(s):
    """Returns True if the string parameter contains a palindrome, False otherwise."""
    if len(s) == 1:
        return True
    elif len(s) == 0:
        return True
    else:
        # probs a classier way to do this but i didnt consent to being alive and my
        # stack on this linux box is like 2^6000000000 so whatever recursion
        if not s[0].isalnum():
            return palindrome(s[1:])
        elif not s[-1].isalnum():
            return palindrome(s[:-1])
        elif s[0] != s[-1]:
            return False
        else:
            return palindrome(s[1:-1])


def main():
    """DO NOT CHANGE THIS CODE"""
    text = input('text?\n')
    if palindrome(text):
        print("Palindrome")
    else:
        print("Emordnilap") # not a palindrome

if __name__ == '__main__':
	main()
