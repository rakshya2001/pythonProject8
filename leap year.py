#check whether the given year is leap or not. if year is leap print'LEAP YEAR'
#esle print"COMMON YEAR".
# Hint: a year is leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
# a year is always a leap year if its number is exactly divisible by 400

year= int(input('Enter the leap year: '))
if year % 4== 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year!! ")
else:
    print(" It is a common year year")

