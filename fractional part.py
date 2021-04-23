#given a positive real number,print its fractional part
import math
val=float(input("Enter the real number:"))
fractional_part=math.modf(val)
print(fractional_part)

#another method

number= float(input("Enter a number  with float: "))
number2= int(number)
divided_number= number-number2
print(f"Fractional part of {number} is {divided_number}")