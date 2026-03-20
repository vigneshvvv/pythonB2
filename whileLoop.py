count = 1

while count <=5:
    # print(count)
    # count = count+1
    count += 1
print("while loop ended")

n =1

while n <= 10:
    if n == 3:
        break
    # print(n)
    n += 1

m = 0
while m <= 10:
    m +=1 
    if m == 3:
        continue
    # print(m)
       
n1 = 1

while n1 <=3:
    # print(n1)
    n1 += 1
else:
    print("This while loop ended correctly")  


def sample():
    print("Hi welcome")


sample()

def printUser(name):
    print(name)
printUser("v")
printUser("m")

def opeartionFunction(num1, num2):
    result = num1*num2
    return result


total  = opeartionFunction(123, 125)
print(total)

def stringConcatination(first_name, last_name):
    full_name = first_name + " "+ last_name
    return full_name


name1 = input("Enter the firstName: ")
name2 = input("Enter the lastName: ")
# name = stringConcatination("new", "name")
name = stringConcatination(name1, name2)
print(name)
