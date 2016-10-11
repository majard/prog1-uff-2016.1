__author__ = '116031030'

def status(gpa):
    if gpa >= 6:
        print('The student has passed.')
    elif gpa <= 4:
        print('The student has failed.')
    else:
        print('The student will need further verification.')

grade = eval(input('What grade did the student get? '))

status(grade)