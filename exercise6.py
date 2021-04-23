#given an integer number, print its last digit.

num=str(input("Enter the number:"))
print(f"the last digit number is {num[-1]}")


#another method
num1=int(input("ENter the number"))
last_digit=num1%10
print(last_digit)