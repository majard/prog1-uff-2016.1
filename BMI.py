height = eval(input('What\'s your height?'))
weight = eval(input('What\'s your weight in kg?'))
BMI = weight / height ** 2
print('Your BMI is:', BMI)
if BMI < 18.5 :
    print('You are underweight.')
elif 18.5 <= BMI < 25 :
    print('You are healthy')
elif 25 <= BMI < 30 :
    print('You are overweight.')
elif 30 <= BMI < 35 :
    print('You have class I obesity.')
elif 35 <= BMI < 40 :
    print('You have class II obesity (severe).')
elif BMI >= 40:
    print('You have class III obesity (morbid)')