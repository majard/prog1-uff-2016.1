fixed = eval(input('Fixed: '))
sales = eval(input('Sales: '))
if sales <= 1000:
    prize = 0
elif sales <= 5000:
    prize = 500
elif sales <= 7500:
    prize = 700
else:
    prize = 1000
print('Salary:', fixed + prize)
print('Prize:', prize)
