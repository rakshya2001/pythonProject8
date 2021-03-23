1.#The python code below calculates the multiplication of 3 upto 10.
# Rewrite the code using recursion.(5)
#code to calculate multipliction of 3.


num=3
for i in range(11):
    product=3*i
    print(f"{num}*{i}={product}")

#what will be the output of the following program?
# Rewrite the code using while loop to display same output

for i in range(5):
    if i==3:
        break
    print(i)

i=0
while i<5:
    if i==3:
        break
    print(i)
    i+=1

#what will be the output of following program? Rewrite the code using for loop

n=5
i=0
while i<=n:
    i+=1
    if i==3:
        continue
    print(i)

for i in range(1,7):
    if i==3:
        i+=1
        continue
    print(i)

# the python code below generates 50 random even integers. Rewrite the code so it uses a while loop instead of for loop.

#import random
#list=[]
#n=50
#i=0
#while i<=n:
    #num=random.randint(1,200)
    #if num % 2==0:
        #list.append(num)
    #i+=1
#extraction method
num= int(input('Enter the number:'))
remainder= num % 10
num1= num//10
remainder1= num1 % 10
num2= num1//10
remainder2= num2 % 10
print(f'the remainder is, {remainder2}')

#using while

num= int(input('Enter the number:'))
while num>0:
    rem=num%10
    print(rem)
    num= num//10

#digit ko sum nikalna parda
sum=0
num= int(input('Enter the number:'))
while num>0:
    rem=num%10
    sum= sum+rem
    num= num//10

print(sum)

#write a program to check a number given by the user is a armstrong number

# sum=0
# num= int(input("Enter the number:")
# a=num
# while num>0:
    # rem= num% 10
    # sum= sum+rem**3
    # num=num//10
# if sum==c:
    # print("yes")
# else:
    # print("no")



