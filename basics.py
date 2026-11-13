
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

# question_1
# WAP to ask the user to enter their 3 favourite movies name and store them in a list and print the list 
movie1 = input("first movie name:")
movie2 = input("second movie name:")
movie3 = input("third movie name:")
your_fav_movies = [movie1, movie2, movie3]
print("your favourite movies are:", your_fav_movies)
movies = []
movies.append(input("enter your 1st favourite movie name:"))
movies.append(input("enter your 2nd favourite movie name:"))
movies.append(input("enter your 3rd favourite movie name:"))
print("your three favourite movies are:", movies)

# question_2
palindrome = list(input("enter anything to check if it's a palindrome: "))
print(palindrome)
palindrome_copy = palindrome.copy()
palindrome_copy.reverse()
print(palindrome_copy)
(palindrome == palindrome_copy)
if (palindrome == palindrome_copy):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")

# ques_3
# WAP to count a number of students with the A grade in a following tuple 
grades = ("c", "d", "a", "a", "b", "b", "a")

grades = ("c", "d", "a", "a", "b", "b", "a")
grades_list = list(grades)
print(grades_list)
grades_list.sort()
print(grades_list)

# DICTIONARY 

about_me = {
    "name" : "Harsh vishwakarma",
    "age" : 18,
    "last_score" : 71.0,
    "studying" : "BTECH AI",
    "subjects" : {
        "sem1" : ["python", "calculus", "english"],
        "sem2" : ["java", "linear algebra", "communication skills"],
        "sem3" : ["c++", "statistics", "data structures"] #nested dictionary
    },
    "learning" : ["python","java", "c++"]
}
about_me["age"] = 19
about_me["hobbies"] = ["cricket", "football", "badminton"]
print(about_me)

dict = {}
dict["name"] = "lakshman"
print(dict)
print(len(list(about_me.keys())))
print(len(list(about_me.values())))
pairs = list(about_me.items())
print(pairs)
print(pairs[5])
print(list(about_me.get("subjects").get("sem2")))
about_me.update({"city" : "indore"})
print((about_me.items()))
