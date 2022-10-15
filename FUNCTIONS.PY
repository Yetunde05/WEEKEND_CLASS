# def fullname(firstname,lastname):
#     print("Your fullname is " + firstname + "," + lastname)
# fullname("yetunde", "olanrewaju")

# firstname = input("enter your firstname:  ")
# lastname = input("enter your lastname: ")
# def fullname(firstname,lastname):
#     print("Your fullname is " + firstname + "," + lastname)
# fullname(firstname,lastname)

# x = int(input('enter a num: '))
# y = int(input('enter the 2nd num: '))
# def num(x,y):
#     ansa = x * y
#     print(ansa)
# num(x,y)
# def my_country(name= "Nigeria"):
#     country = "I am from " + name
#     return country
    

# print(my_country('italy'))
    
# # TO PASS A DEFAULT VALUE

# x = list(map(int,input("Enter three numbers:").split()))
# def duplicate(x):
#     y = []
#     for i in x:
#         new = i * 2
#         y.append(new)
#     return y
# print(duplicate(x)) 

import string


# write a function that returns the length of a string, the string
# should be a users input
# hi = input("Enter any word: ")
# def word():
#     print(len(hi))
# word()

# write a function that returns the max number in x, x should be a list
# x = list(map(int,input("Enter three numbers:").split()))
# def find_maximum (x):
#     ans = max(x)
#     return ans
# write a function that returns the min number in x, x should be a list
x = list(map(int,input("Enter three numbers:").split()))
def find_minimum (x):
    ans = min(x)
    print(ans)
    # return ans
find_minimum(x)

    




    

