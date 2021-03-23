#for given integer x, print"true" if it is positive, print "false" if it is negative and print "zero"
#if it is 0

num=int(input("Enter the number:"))
if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is negative number")
elif num==0:
    print(f"{num} is zero")
else:
    print(f"given data is invalid")