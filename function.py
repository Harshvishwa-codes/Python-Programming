# function in python 

# before

a = 10
b = 20
print(a + b)

# now with the help of function

def calc_sum(a, b):
    sum = a + b 
    print(sum) 
    return sum 


# 2
# calc_sum(55, 88)

# in more simple way
#function definition
def calc_sum(a, b):#parameters
    return a + b 

sum = calc_sum(10, 20) #function call ; arguments
print(sum)


# average of 3 no. using function

def calc_average(a, b, c): 
    sum = a + b + c 
    avg = sum / 3 
    print(avg)
calc_average(1, 2, 3)

# average of 3 no. 2nd method 

def calc_avg(a, b, c):
    sum = a+b+c 
    avg = sum / 3
    print("the average of three no. is =>", avg)
    return(avg)

calc_avg(int(input("enter first no.")),int(input("enter second no.")),int(input("enter third no.")),)

# question 1 of function

# WAF to print the length of a list (list is a perameter )
name = ["mahendra", "sunita", "himansh", "harsh"]
age = [40, 36, 22, 18]

def info (list):
    print(len(list))

info(name)
info(age)

# que 2
# WAF to print the elements of a list in a single line. (list is a parameter)

name = ["mahendra", "sunita", "himansh", "harsh"]
age = [40, 36, 22, 18]

def print_line (list):
    for item in list:
        print(item, end="\n")
print_line(name) 
print_line(age)




age = [40, 36, 22, 18]
name = ["mahendra", "sunita", "himansh", "harsh"]
def line(list):
    for item in list:
        print(item, end="  \n")
line(age)
print("\n")
line(name)

# que 3
# WAF to find the factorial of n.(n is a parameter)



def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

x = int(input("enter a no."))
calc_fact(x)

# WAF to covert USD to INR
def converter(USD):
    INR = USD*95.11
    print(USD, "$" ,"=", INR, "₹")

x = int(input("enter USD to convert into INR:"))
converter(x)

# WAF to check a no. even or odd

def check(x):
    if x % 2 == 0 :
        print("even")
    else :
        print("odd")
i = int(input("enter a no, to check the no. is even or odd : "))
check(i)
