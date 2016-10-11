day = eval(input('What day were you born? '))
month = eval(input('What month were you born? '))
year = eval(input('What year were you born? '))
if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
    print('You are an Aries!')
elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
    print('You are a Taurus!')
elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and month == 6):
    print('You are a Gemini!')
elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
    print('You are a Cancer!')
elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
    print('You are a Leo!')
elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and month == 9):
    print(('You are a Virgo!!'))
elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
    print('You are a Libra!')
elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and month == 11):
    print('You are a Scorpio!')
elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
    print('You are a Sagittarius!')
elif (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and month == 1):
    print('You are a Capricorn!')
elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
    print('You are an Aquarius!')
elif ((19 <= day <= 28 and month == 2)
      #check if it's a leap year:
      or (day == 29 and month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
      or (1 <= day <= 20 and month == 3)):
    print('You are a Pisces!')
#if no condition was met, the date wasn't valid:
else:
    print('Input valid numeric dates')