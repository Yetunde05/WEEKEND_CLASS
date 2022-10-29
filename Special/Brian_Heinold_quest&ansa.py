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
print(ques1,ques1*2,ques1*3,ques1*4,ques1*5, sep="---") 

# 7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There
# are 2.2 pounds in a kilogram
# solution

user = eval(input("input your weight in kilo: "))
output = user*2.2
print(f"You have {output} weight, which have been converted to pounds" )

# 8. Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.
# solution
questn1 = eval(input("Enter a number: "))
questn2 = eval(input("Enter the 2nd number: "))
questn3 = eval(input("Enter the 3rd number: "))
total = questn1 + questn2 + questn3
average = total/2
print(total)
print(int(average))

# 9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# the percent tip they want to leave. Then print both the tip amount and the total bill with the
# tip included
# solution

meal_price = eval(input('Enter the price of meal: '))
tip_amount = float(input('Enter percent tips amount: '))
print(meal_price*tip_amount/100)



