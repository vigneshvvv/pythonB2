a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))

option = int(input("Enter operation you wish to perform: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

if option == 1:
    print("The Sum of Value A and B is ", a+b)
elif option ==2:
    if a >b:
        print("The Difference of Value A and B is", a-b)
    elif a <b:
        print("The Difference of Value A and B is", b-a)
    else:
        print("The Difference of Value A and B is", a-b)        
    
elif option == 3:
    print("The product of Value A and B is ", a*b)
elif option ==4:
    print("The division of value A and B is ", a/b)
else:
    print("invalid Operation! pls enter a valid one")





