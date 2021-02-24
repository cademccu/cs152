# Triangle Properties
# 
# This program:
# * prompts for a filename
# * prints a heading for the output
# * prints a line with the side and triangle properties for each triangle in the file
#
# Refer to the above description for definitions of triangles/angles

def side(a, b, c):
    """
    Returns 'scalene', 'isosceles', 'equilateral', or 'none'
    based on the triangle side relationships given the lengths of the sides.
    """
    # add code to return the correct side relationship
    if a == b and b == c:
        # something something transitive? idc
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"



def angle(a, b, c):
    """
    Returns 'acute', 'obtuse', 'right', or 'none'
    based on the triangle angle relationships given the lengths of the sides
    where c is the longest side.
    """
    # add code to return the correct angle relationship
    left = a**2 + b**2
    right = c**2

    if left > right:
        return "acute"
    elif left == right:
        return "right"
    else:
        return "obtuse"


def triangle_properties(sides):
    """
    Returns a properly formatted string containing the triangle properties
    from a list of strings containing the lengths of the sides.
    """
    # Don't change this code that figures out the longest side.
    abc = [int(sides[0]),int(sides[1]),int(sides[2])]
    c = max(abc)
    abc.remove(c)
    a = abc[0]
    b = abc[1]
    # add code to return a properly formatted string that matches the column headings
    return "{:>3} {:>3} {:>3} {:<5} {:<4}".format(c, b, a, angle(a, b, c)[:5], side(a, b, c)[:4])
    




def column_headings():
    """
    Return a string containing the column headings.
    DO NOT CHANGE THIS CODE
    """
    return '111 222 333 angle side'


def triangles(filename):
    """
    Prints column headings and a line containing the properties of each triangle in the file.
    """
    print(column_headings())
    # add code to process the file, printing the triangle properties for each line in file
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        print(triangle_properties(line.split()))

def main():
    """
    Prompts for filename and processes the file.
    DO NOT CHANGE THIS CODE
    """
    filename = input('filename?\n')
    triangles(filename)


if __name__ == '__main__':
    main()
