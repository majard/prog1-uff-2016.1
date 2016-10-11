def add_new_name(name, numbers, phonebook):
    phonebook[name] = numbers

    return phonebook


def add_number(name, number, phonebook):
    if name in phonebook:
        phonebook[name] += number

    else:
        opt = input('There is no {} in the phonebook. Do you want to add this person (y/n)?'.format(name))

        if opt == 'y':
            add_new_name(name, number, phonebook)

    return phonebook


def delete_number(name, number, phonebook):
    if len(phonebook[name]) == 1:
        phonebook.pop(name)

    elif number in phonebook[name]:
        phonebook[name].remove(number)

    else:
        print('There is no such number under {}'.format(name))

    return phonebook


def delete_name(name, phonebook):
    if name in phonebook:
        phonebook.pop(name)

    else:
        print('There is no {} in the phonebook.'.format(name))

    return phonebook


def check_name(name, phonebook):
    if name in phonebook:
        print(phonebook[name])

    else:
        print('There is no {} in the phonebook.'.format(name))


def menu():
    print('\nChoose an option:')
    print('1 - add name\n'
          '2 - add number\n'
          '3 - delete phone number\n'
          '4 - delete name\n'
          '5 - check phone number\n'
          '6 - exit')
    return int(input())


def input_name():
    return input('Name: ')


def input_numbers():
    return input('Numbers (separated by comma): ').split(',')


def main():
    phonebook = {}
    opt = 0

    while opt != 6:
        opt = menu()

        if opt == 1:
            name = input_name()
            numbers = input_numbers()
            phonebook = add_new_name(name, numbers, phonebook)

        elif opt == 2:
            name = input_name()
            numbers = input_numbers()
            phonebook = add_number(name, numbers, phonebook)

        elif opt == 3:
            name = input_name()
            numbers = input_numbers()
            phonebook = delete_number(name, numbers[0], phonebook)

        elif opt == 4:
            name = input_name()
            phonebook = delete_name(name, phonebook)

        elif opt == 5:
            name = input_name()
            check_name(name, phonebook)

main()