# OOPs concept
# (object oriented programming)

class Student:

    # # default constructer 
    # def __init__(self):
    #     pass
    school_name =" ICS "
    # parameterized constructer
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student data in database...")

    def Wellcome(self):
        print("wellcome to ICS, Here your future is brighter than other's, ", self.name, self.marks)

S1 = Student("Harsh", 71)
S1.Wellcome()

S2 = Student("Akshatra", 76)
S2.Wellcome()

S3 = Student("Sarthak", 65)
S3.Wellcome()

S4 = Student("Anish", 78)
S4.Wellcome()

S5 = Student("Yashraj", 77)
S5.Wellcome()

print(S1.wellcome , S1.name, S1.marks, S5.school_name)
print(S2.name, S2.marks, S5.school_name)
print(S3.name, S3.marks, S5.school_name)
print(S4.name, S4.marks, S5.school_name)
print(S4.name, S4.marks, S5.school_name)
print(S5.name, S2.marks, S5.school_name)



# # que. 1 

class Student:
    def __init__ (self, name , marks):
        self.name = name 
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hello,", self.name,"your avg marks is :",  sum/3)


s1 = Student("jassi singh",[98, 90, 88])
s1.get_avg()

s2 = Student("mahesh jatt", [44, 50, 98])
s2.get_avg()

class Employs:
    def  __init__ (self, name, degree, age):
        self.name = name 
        self.degree = degree
        self.age = age
    @staticmethod
    def hello():
        print("hello")
    def check_pass(self):
        if self.age >= 18:
            return("wellcome to vishwa group of technologies, you are eligible to apply")
        else:
            return "you are not eligible"


E1 = Employs("harshad mehta", "BTECH" , 22 )
print(E1.check_pass())

E1.age = 25
print(E1.check_pass())

E1.hello()


class Account :
    def __init__(self, name, account_no, balance, password):
        self.name = name
        self.acc_no = account_no
        self.bal = balance
        self.__acc_pass = password

    # pass
    def get_pass(self):
        print(self.__acc_pass)

    # debit method
    def debit(self, amount):
        self.bal -= amount
        print("₹", amount, "was debited from your account")
        print("your current balance is = ₹", self.bal)

    # credit method
    def credit(self, amount):
        self.bal += amount
        print("₹", amount, "was credit in your account")
        print("your current balance is = ₹", self.bal)

    # balance
    def balance(self):
        return self.balance 

acc1 = Account("harsh vishwakarma", 9111659969, 100000, "abcde")

acc1.debit(50000)

acc1.credit(100000)

acc1.balance()

acc1.get_pass()

acc1.credit(2500000)

acc1.debit(2600000)

class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")

class Toyotacar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

class Maruticar(Car):
    def __init__(self, name, type):
        self.name = name 
        super().__init__(type)

c1 = Toyotacar("innova", "petrol")
print(c1.name, c1.type)

c1 = Maruticar("swift", "electric")
print(c1.name,c1.type)



class Person:
    name = "pappu"

    def changeName(self, name):
        self.__class__.name= name 

p = Person()
p.changeName("appu")
print(p.name)
print(Person.name)




class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) /3) + "%"


s1 = Student(55, 65, 90)
print(s1.percentage)

s1.phy = 99
print(s1.percentage)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "i + ", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal ,newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal ,newImg)
    
num1 = Complex(2, 3)
num1.showNum()

num2 = Complex(4, 5)
num2.showNum()

num3 = num1 + num2
num3.showNum() 

num3 = num1 - num2
num3.showNum() 


# que 1 

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# que 2 

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "100000")

e1 = Engineer("harsh", 22)
e1.showDetails()


class Order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price



ord1 = Order("biscuit", 20)
ord2 = Order("tea", 15)

print(ord1>ord2)

# oops revision  
# polymopism


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2

class Rectangle(Shape) :
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

c = Circle(12)
a = Circle(22)
print(c.area())
print(a.area())

r = Rectangle(5, 7)
print(r.area())
