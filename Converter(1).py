option = input('What conversion do you wish to make:\n'
               '1 - Celsius to Fahrenheit\n'
               '2 - Fahrenheit to Celsius\n'
               '3 - Inches to millimeters\n'
               '4 - Millimiters to inches\n')
value = eval(input('Enter the value: '))
if option == '1':
    print('Temperature in Fahrenheit: ', (9/5) * value + 32)
elif option == '2':
    print('Temperature in Celsius: ', (value - 32) * (5/9))
elif option == '3':
    print('Value in millimeters: ', value * 24.5)
elif option == '4':
    print('Value in inches: ', value / 24.5)
else:
    print('Invalid option. Input an integer between 1 and 5 as first variable.')