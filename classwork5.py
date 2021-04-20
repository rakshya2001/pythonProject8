def greeter(name):
    print("Good morning")
    print("Hello"+ str(name))
print("go")
greeter("World")


#another program
a=[2,3,4]
b=a
a.append(5)
print(a)
print(b)

#another
a=[2,3,4]
b=a.copy()
a.append(5)
print(a)
print(b)

#another

l=[2,7,8,[10,11,12],4,5]
print(l[1])
print(l[3][2])

#another
r=(4,5)
print(type(r))