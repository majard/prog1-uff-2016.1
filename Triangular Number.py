number = eval(input('Input a number: '))
multiple = 0
counter = 1
while multiple < number:
    multiple = aux = counter
    for i in range(2):
        aux += 1
        multiple *= aux
    counter += 1
if multiple == number:
    print('This is a triangular number.')
else:
    print('This is not a triangular number.')