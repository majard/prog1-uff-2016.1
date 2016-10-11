c1 = input('Client 1: ')
value1 = eval(input('Value in reais client 1 spent: '))
c2 = input('Client 2: ')
value2 = eval(input('Value in reais Client 2 spent: '))
c3 = input('Client 3: ')
value3 = eval(input('Value in reais Client 3 spent: '))
print('Total: ', value1 + value2 + value3)
print('Average purchase value: ', (value1 + value2 + value3) / 3 )
str = 'Clients that bought 100 reais or more: \n'
if value1 > 100:
    str += c1 + '\n'
if value2 > 100:
    str += c2 + '\n'
if value3 > 100:
    str += c3
print(str)
counter = 0
if value1 < 50:
    counter += 1
if value2 < 50:
    counter += 1
if value3 < 50:
    counter += 1
if counter == 0:
    print('No one bought less than 50 reais')
elif counter == 1:
    print('One person bought less than 50 reais')
else:
    print(counter, 'people bought less than 50 reais.')