__author__ = '116031030'

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    return a / b

def menu():
    print('Mem = {}'.format(mem))
    print('1 - Add')
    print('2 - Subtract')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Clean Memory')
    print('6 - Exit the program')

mem = 0
opt = 0
b = 0
num = 0

while opt != 6:
    menu()
    opt = int(input('Choose an option: '))
    if opt != 6 and opt != 5:
        num = eval(input('Input second term: '))
    if opt == 1:
        mem = add(mem, num)
    elif opt == 2:
        mem = sub(mem, num)
    elif opt == 3:
        mem = multiply(mem, num)
    elif opt == 4:
        mem = div(mem, num)
    elif opt == 5:
        mem = 0
