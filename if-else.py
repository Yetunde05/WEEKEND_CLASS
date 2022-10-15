name = input("enter your name: ")
age = int(input("enter your age: "))

if age>=0 and age<=4:
    print(f"hello {name}, You are still a baby")
elif age>=5 and age<=12:
    print(f"hello {name}, You are a child")
elif age>=13 and age<19:
    print(f"hello {name}, You are a teenager")
elif age>=20 and age<=50:
    print(f"hello {name}, you are an adult")
elif age>=51:
    print(f"hello {name}, You are Elderly")
else:
    print("invalid username or passord")


username = "yetunde2022"
password = "12345678"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print(f"hello{input_username}, login successful")
else:
    print("invalid username or password")
     