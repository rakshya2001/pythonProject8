#wap to sum of three given integers. However, if two values are equal sum will be zero.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1==num2 or num1==num3 or num2==num3:
    print(f"Its {sum} is zero")
else:
    add=num1+num2+num3
    print(add)

#another
def sum(a,b,c):
    if a==b or b==c or c==a:
        sum = 0
    else:
        sum=(a+b+c)
    return sum


x,y,z = [int(a) for a in input ("Enter three number:").split(",")]

print(sum(x,y,z))