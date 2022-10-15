import string
import random
password_character = list(string.ascii_letters + string.digits + "!@#$%^&*()")
pass_length = int(input("Enter password length: "))
password = []
for i in range(pass_length):
		password.append(random.choice(password_character))
print("".join(password))


# TASK 1Write a python program that will generate a random password of any length for a user.
# The program should first ask the user for the length of the password, and then generate a password of that length.
# Hint: Use python random module to generate random numbers



