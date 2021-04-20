#given a three-digit number. Find the sum of it digit


number = int(input("Enter the number:"))
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)