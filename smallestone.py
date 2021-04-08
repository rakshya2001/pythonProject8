#give three integers, print the smallest one(three integers should be user input)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1<num2:
    print(f"{num1} is smallest one!")
elif num2<num3:
    print(f"{num2} is smallest one")
else:
    print(f"{num3} is the smallest")

