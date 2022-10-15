# a. Write a program to perform the following:
# i.  receive the full name, age and location from a user.
# ii. print out a description message to the user using f strings. The mesage should look like this:
#     Hello <full name>
#     I see you are <age> years old and you reside in <location>
#     NOTE: the full name should be in lower case (use string method)
 
fullname = input('fullname:')
Age = input('Age:')
Location = input('Location:')
print(f'Hello {fullname.lower()}\nI see you are {Age}, years old and you reside in {Location}')

# b. Write a program that will take request for a user's name and then print the following:
#  i. the complete name
# ii. the length of the name
# iii. the last character of the name 
Fullname = input('Fullname:')
print(len(Fullname))
print(Fullname[-1])