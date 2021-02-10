# MadLibs from a file

def madlib_word(word):
    """Returns a substitution for a fill-in-the-blank or the original word."""
    if word[0] == "_" == word[-1]:
        return input(word[1:-1].replace("_", " ")+'?\n')
    else:
        return word


def madlib_line(text):
    """Returns a string containing the line with the fill-in-the-blanks substituted."""
    words = text.split()  # try printing this to see what it does
    # process all the words in the line and return a string - hint use madlib_word
    r_string = ""
    for word in words:
        r_string += madlib_word(word)
        r_string += " "
    return r_string


def madlib_file(filename):
    """Reads the madlib file and returns the completed madlib as a list of strings."""
    # process all the lines in the file and return a list of strings - hint use madlib_line
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = madlib_line(lines[i])

    return lines


def madlib_print(madlib):
    """Prints a completed MadLib, line by line."""
    # print the strings in the list
    for x in madlib:
        print(x)
    return


def main():
    """Completes the user supplied madlib."""
    filename = input("MadLib filename?\n")
    madlib_print(madlib_file(filename))


# Do not change the following lines or the tests will fail.
if __name__ == '__main__':
    main()
