empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))1

tuple1 = (1,2,3,"Hi")
# print(tuple1)

tuple2 = 1,2,3,"Hi"
# print(tuple2)

tuple2 = (12)
# print(tuple2)

tuple3 = (12,)
# print(tuple3)

tuple4 = (10,20,30,10)
print(tuple4[1])
print(tuple4[-1])
print(tuple4[-2])
print(tuple4[1:3]) #to print range of element 
print(len(tuple4)) #to find length of tuple
print(max(tuple4)) #to find maximum element in tuple
print(min(tuple4)) #to find minimum element in tuple
print(tuple4.count(10)) #to find numer of time a element printed in tuple

for s in tuple4: #iterating a tuple using for loop
    print(s)