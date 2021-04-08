#2. WAP which accepts marks of four subjects and displays total marks, percentage and grade.
# Hint: more than 70%--> distinction, more than 60%-->first, more than 40%-->pass, less than 40%--> fail

subject1=float(input('Enter the marks of first subject'))
subject2=float(input('Enter the marks of second subject'))
subject3=float(input('Enter the marks of third subject'))
subject4=float(input('Enter the marks of fourth subject'))
total_marks= subject1+subject2+subject3+subject4
percentage= (total_marks)*100//400
hello=print(percentage)
if percentage>70:
    print('Distinction')
if percentage>60:
    print("First")
if percentage>40:
    print("Pass")
else:
    print('Fail')