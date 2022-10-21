# 1. Print a box like the one below.
# *******************
# *******************
# *******************
# *******************
# solution
from math import sqrt


print("*******************\n*******************\n*******************\n*******************")

# 2. Print a box like the one below.
# *******************
# * *
# * *
# *******************
# solution
print("*******************\n* *\n* *\n*******************")

# 3. Print a triangle like the one below.
# *
# **
# ***
# ****
# solution
print("*\n**\n***\n****")

# 4. Write a program that computes and prints the result of 512 − 282/
# 47 · 48 + 5
# . It is roughly .1017
# solution
a = 512-282
b = (47*48)+5
ansa = a/b
print(ansa)

# 5. Ask the user to enter a number. Print out the square of the number,print it out in a full sentence that ends in a period.
# solution
ques = int(input("Enter a number: "))
num = ques*ques
print(f"You have {num} subjects in a period.")

# 6. Ask the user to enter a number x.print out x, 2x, 3x, 4x,
# and 5x, each separated by three dashes, like below.
# Enter a number: 7
# 7---14---21---28---35
# solution
ques1 = int(input("Enter a number: "))
print(ques1,'---',ques1*2,"---",ques1*3,"---",ques1*4,"---",ques1*5)



