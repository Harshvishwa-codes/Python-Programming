
# RecursionError
# recursive function

def show(n):
    if (n == 0): #base case 
        return
    print(n)
    show(n-1)
    print("harsh")
show(5)

# factorial using recursion

def fact(n):
    if(n == 0 or n == 1 ):
        return 1 
    return fact(n-1) * n
print(fact(5))

# questions 

# 1. write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if (n == 0):
        return 0
    return sum(n-1) + n
print(sum(50))

# 2.write a recursive function to print all element in a list. 
# hint: use list & index as a parameters 

def ele(list, idx=0):
    if idx == len(list) :
        return 
    print(list[idx])
    ele(list, idx + 1)

age = [18, 22, 35, 40]
ele(age)
