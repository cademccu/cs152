def get_grades():
    count = int(input("How many grades:\n"))
    grades = []
    for i in range(count):
        grades.append(float(input("Enter grade:\n")))
    return grades

def average(grades):
    total = 0
    for i in grades:
        total += i
    return total / len(grades)

def maximum(grades):
    m = -999999
    for g in grades:
        if g > m:
            m = g
    return m

def minimum(grades):
    m = 999999
    for g in grades:
        if g < m:
            m = g
    return m

def print_grades(grades):
    for g in grades:
        print(g)

def main():
    grades = get_grades()

    print_grades(grades)
    print("Average:", average(grades))
    print("Max:", maximum(grades))
    print("Min:", minimum(grades))

if __name__=="__main__":
    main()
