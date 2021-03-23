#addition
def sum():
   a= int(input("Enter the first number:"))
   b= int(input("Enter the second number:"))
   print(f"The sum of {a} and {b} is {a+b}")

sum()

#subtraction
def sub(a, b):
    print(f"The subtraction of {a} and {b} is {a - b}")


sub(8,5)

#multiplication
def mul():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    return a * b


c = mul()
print(c)

#division
def div(x,y):
    return x//y

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c=div(8,4)
print(c)

#write a program to find out a factorial of a number by using functions:
def fact(a):
    product = 1
    for i in range(2, num + 1):
        product = product * i
    return a


num=int(input("Enter a number for factorial"))
print(fact(a))


#write a program to print a multiplication table of a given number by using a fucntion\

def mul_tab(num):
    for i in range(1,11):
        product=num*i
        print(f'{num}*{i}={product}')


num=int(input("Enter number for multiplication"))
mul_tab(num)
