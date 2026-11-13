
# list
list1 = [1, 2, 3, 47, 5, 6, 7, 8, 9 ]
print(list1)
print(type(list1))
print(list1[4]) 
list1[2] = 100
print(list1)

#slicing
print(list1[1:4])
print(list1[2:])
# print(list1[-4:-1])

list1.append("harsh")
print(list1)
# list.sort()
print(list1)
list1 = [1, 2, 3, 5, 6, 7, 8, 9 ]
list1.insert(3, 4)
list1.append(10)
list1.insert(1,143)
list1.remove(3)
list1.pop(1)
list1.insert(2, 3)
list1.reverse()
print(list1)
list1[0] = 200
print(list1)

# tuple
tup = (1, 2, 3, 5, 9, 20)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1:4])
print(tup.index(20))
print(tup.count(3))
