def include_grades(grades):
    temp = {}
    name = input('Student name: ')
    while name != '':
        grade1 = eval(input('Input first grade: '))
        grade2 = eval(input('Input second grade: '))
        temp[name] = [grade1, grade2]
        name = input('Student name: ')

    grades.update(temp)

    return grades

def calculate_average(grades):
    name = input('Name of the student: ')
    average = sum(grades[name])/len(grades[name])
    return average

def menu():
    print('Choose an option: ')
    print('1 - Show grades')
    print('2 - Include grades ')
    print('3 - calculate average')
    print('4 - exit')
    return int(input())

def main():
    opt = 0
    grades = {}
    while opt != 4:
        opt = menu()
        if opt == 1:
            print(grades)
        elif opt == 2:
            grades = include_grades(grades)
        elif opt == 3:
            print(calculate_average(grades))

main()