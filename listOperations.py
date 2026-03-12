# to add value in list
my_list = [1,2,3]
my_list.append(4)
# print(my_list)

# to add value based on index
my_listNew = [1,2,4]
my_listNew.insert(2, 3)
# print(my_listNew)

# to merge two list using extend
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
# print(list1)

# to combine two list into one new list
new_list = list1 + list2
# print(new_list)

# to remove element from list based on index
list1.remove(2)
# print(list1)

# removing element using pop option with index
removed_value= list1.pop(0)
print(list1)
print(removed_value)

# removing last element from list using pop
pop_new = list1.pop()
print(pop_new)

# to delete all the  values in list
list1.clear()
print(list1)

# delete element based on index using del
list3 = [1,2,3,4,5,6]
del list3[1]
print(list3)

# to delete rande of element from list using del
del list3[1:4]
print(list3)

# edit a value in particular index
list4 = [10,20,30,40]
list4[1] = 50
print(list4)

# edit mutiple elements using range 
list4[1:3] = [20,30]
print(list4)

# to get value from list using index
print(list4[0])

