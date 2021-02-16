# sudoku checker
# I'm lazy.  let's write something to check sudokus.
# To be solved, each row, column, and 3x3 grid must be valid.
# Valid means contains each of the values 1, 2, 3, 4, 5, 6, 7, 8, 9.

valid = [1,2,3,4,5,6,7,8,9]


def get_sudoku(filename):
    """
    Returns a two dimenional list structure containing the 9x9 sudoku.
    DO NOT CHANGE THIS CODE
    """
    grid = []
    with open(filename,'r') as file:
        for line in file:
            grid.append([int(i) for i in line.split(' ')])
    return grid


def I_am_so_tired_of_not_copying_by_value(s):
    r = []
    for x in s:
        r.append(x[:])
    return r



def okrows(sudoku):
    """Returns true only if each of the rows in the sudoku is valid. 
    i.e each row contains numbers between 1-9"""
    # your code here
    s = I_am_so_tired_of_not_copying_by_value(sudoku)
    for row in s:
        row.sort()
        if row != valid:
            return False
    return True


def okcols(sudoku):
    """Returns true only if each of the columns in the sudoku is valid.
    i.e each column contains numbers between 1-9"""
    # your code here

    s = I_am_so_tired_of_not_copying_by_value(sudoku)
    for i in range(9):
        temp = []
        for row in s:
            temp.append(row[i])
        temp.sort()
        if temp != valid:
            return False

    return True


def okgrid(sudoku,r,c):
    """Returns true if a 3x3 subgrid located from r,c to r+2,c+2 is valid."""
    # your code here
    s = I_am_so_tired_of_not_copying_by_value(sudoku)
    temp = []
    for i in range(r, r+3):
        for ii in range(c, c+3):
            temp.append(s[i][ii])
    temp.sort()
    if temp != valid:
        return False
    return True


def okgrids(sudoku):
    """
    Returns true only if each of the nine 3x3 grids in the sudoku are valid.
    DO NOT CHANGE THIS CODE
    """
    for r in range(0,9,3):
        for c in range(0,9,3):
            ok = okgrid(sudoku,r,c)
            if not ok:
                return False
    return True


def main():
    """
    Tells us if we have solved a sudoku.
    DO NOT CHANGE THIS CODE
    """
    #prompt the user for filename
    filename = input('filename?\n')
    sudoku = get_sudoku(filename)
    solved = [okrows(sudoku), okcols(sudoku), okgrids(sudoku)]
    #all function acts like an 'and' operator
    #all(solved) gives you a boolean value of - (okrows(sudoku) and okcols(sudoku) and okgrids(sudoku))
    print(solved,all(solved))


if __name__ == '__main__':
    main()
