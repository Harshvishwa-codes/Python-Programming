
# loops
# while loop
count = 1 
while count <= 5:
    print("hello Harsh ji")
    count += 1

# question 1 
# print no. from 1 to 100
x = 1
while x <= 100 :
    print (x)
    x += 1 
print("loop end ")

# que .2 
# print no. from 100 to 1
i = 100
while i >= 1 :
    print(i)
    i -= 1 
print("program end")

# que no. 3 
# print multiplication table of no. N
x = int(input("enter any no. to find whose table:"))
m = 1
while m<=10:
    print(x*m)
    m += 1
print("your table is here")

# print the element of the following list using a loop 

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
# assets = ["lap", "mob", "buds"]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
#traverse
idx = 0 #initialization
while idx < (len(list)):
    print(list[idx])
    idx += 1

# ques.4
# search for a number x in this tuple using loop 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )
x = 16
i = 0 
while i < len(list):
    if list[i] == x :
        print("found at index:", i)
    i += 1 
print("program end")


# break key 
x = 0
while x <= 10:
    print(x)
    if (x == 5):
        break
    x += 1 

# continue key 
i = 0 
while i <= 10:
    if (i%2 != 0 ):
        i += 1 
        continue  #skip
    print(i)
    i += 1

# for loop  
str = "apna ghar"
for seq in str :
    if (seq == 'h'):
        print("found 'h' ")
        break
    print(seq)
else: 
    print("hoga")

# que 1 of for loop
# print the elements of list using a loop
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for x in list:
    print(x) 

# que . 2 
# search for a number x in this tuple using a loop

nums = [1, 4, 9, 16, 25, 36, 49, 4, 64, 81, 100, 4]
y = 25
idx = 0
for x in nums:
    if (x == y):
        print("no. found at idx:", idx)
        break
    idx += 1 
