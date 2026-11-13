# file handling input/output


# f = open(r"C:\Users\ACER\OneDrive\Desktop\Harsh.py\demo.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f = open(r"C:\Users\ACER\OneDrive\Desktop\Harsh.py\demo.txt", "a")
# f.write("\nI am now learning Java and enlish also .")
# f.close

with open("demo.txt", "w")as f:
    f.write("i am harsh.V")


import os
os.remove("demo.txt")


# practice questions 
def replace_word():
    with open("practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("JAVA","PYTHON")
    print(new_data)
    with open("practice.txt","w") as f:
        data = f.write(new_data)

replace_word()


def check_for_word():
    word = "learning"
    with open("practice.txt","r")as f:
        data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

check_for_word()


def check_word_line():
    word = "learning"
    with open("practice.txt","r") as f:
        line1 = f.readline()
        if(line1.find(word) != -1):
            print("word exist in 1st line")
        else:
            print(-1)
    
        line2 = f.readline()
        if(line2.find(word) != -1):
            print("word exist in 2nd line")
        else:
            print(-1)

check_word_line()




def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                return line_no
            line_no += 1
    return -1
print(check_for_line())



with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            print(int(num))
            num = ""
        else :
            num  += data[i]



count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for i in nums:
        if (int(i) % 2 == 0):
            count += 1
print(count)


