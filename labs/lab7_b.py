def sum_list(l):
    x = 0.0
    for i in l:
        x += i

    return x

def every_other(start,end):
    x = []
    if start > end:
        return x
    else:
        for i in range(start, end + 1, 2):
            x.append(i)
            
    return x

def count(item, container):
    count = 0
    for obj in container:
        if item == obj:
            count += 1
    return count
    
def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return False
    count = 0
    for c in string1:
        if c != string2[count]:
            return False
        count += 1
    return True
        
def print_grid(rows,cols):
    for i in range(rows):
        print("#" * cols) # no nesting today
        
# Test your code in main
def main():
    print(sum_list([2,4,5.5, 9, -10]))
    print(every_other(1,10))
    print(every_other(4,8))
    print(count('a','banana'))
    print(count(8, [ 4, 6, 8, 80, 2, 8 ]))
    print(compare_strings("Orange", "orange"))
    print(compare_strings("App", 'Application'))
    print_grid(4,4)
    print_grid(2,8)

# Do not change the code below
if "__main__" == __name__:
    main()
