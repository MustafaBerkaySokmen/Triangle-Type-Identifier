#This file is for the Tryangle Types question.
a=float(input("Enter the length of the first side:"))
b=float(input("Enter the length of the second side:"))
c=float(input("Enter the length of the third side:"))
if a+b>c and a+c>b and b+c>a:
    if c==max(a,b,c):
        if c**2<a**2+b**2:
            print("Acute triangle")
        elif c**2==a**2+b**2:  
            print("Right triangle")
        else:
            print("Obtuse triangle")
    elif b==max(a,b,c):   
        if b**2<a**2+c**2:
            print("Acute triangle")
        elif b**2==a**2+c**2:  
            print("Right triangle")
        else:
            print("Obtuse triangle")
    elif a==max(a,b,c):
        if a**2<c**2+b**2:
            print("Acute triangle")
        elif a**2==c**2+b**2:  
            print("Right triangle")
        else:
            print("Obtuse triangle")
else:
    print("Not a valid triangle")




