#Game finding a secret number within 3 attempts using while loop
num=3
j=3
i=1
while i<=3:
    val=int(input("Enter the number:"))
    j=j-1
    if val==num:
        print(f'The number you have guessed is correct')
    else:
        print(f'Try again!!,you have {j} attempt left')
    i=i+1

#using random
import random
answer= random.randint(0,10)
num=3
i=1
while i<=3:
    val=int(input("Enter the number:"))
    if val==num:
        print(f'The number you have guessed is correct')
    else:
        print(f'Try again!!,')
    i=i+1