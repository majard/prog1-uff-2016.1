fixed = eval(input('Fixed: '))
sales = eval(input('Sales: '))
if sales <= 1000:
    prize = 0
elif sales <= 5000:
    prize = 500.00
elif sales <= 7500:
    prize = 700.00
else:
    prize = 1000.00
print('Salary:', fixed + prize)
print('Prize:', prize)
