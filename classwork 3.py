def add():
   print("function start")
   a=int(input("Enter first number:"))
   b=int(input("Enter second number:"))
   c=a+b
   print(c)
   print("function end")

print("Main start")
print("Function is calling")
add()
print('program end')

#another method
def add(a,b):
   print("function start")
   c=a+b
   return c

print("Main start")
print("Function is calling")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
ans=add(a,b)
print("the sum is", ans)
print('program end')