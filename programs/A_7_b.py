# NO FOR LOOPS :(

def average(grades):
    if len(grades) == 0:
        return 0
    start = 0
    i = 0
    while i != len(grades):
        start += grades[i]
        i += 1
    return start / len(grades)

def maximum(grades):
    if len(grades) == 0:
        return 0
    i = 0
    maximum = grades[0]
    while i != len(grades):
        if grades[i] > maximum:
            maximum = grades[i]
        i += 1
    return maximum

def minimum(grades):
    if len(grades) == 0:
        return 0
    i = 0
    minimum = 999999.0
    while i != len(grades):
        if minimum > grades[i]:
            minimum = grades[i]
        i += 1
    return minimum
    

def print_grades(grades):
    i = 0
    while i != len(grades):
        print(grades[i])
        i += 1

def get_grades():
    num = float(input("Enter grade:\n"))
    grades = []
    while num >= 0:
        grades.append(num)
        num = float(input("Enter grade:\n"))
    return grades

def main():
    grades = get_grades()
    print_grades(grades)
    print("Average: " + str(average(grades)))
    print("Max: " + str(maximum(grades)))
    print("Min: " + str(minimum(grades)))
    
    
if __name__ == "__main__":
    main()
