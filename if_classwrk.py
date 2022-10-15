name = input("Enter your name :")
score = int(input("Enter your score: "))
if score>=70 and score<=100:
    print(f"hello {name}, your grade is A")
elif score>=60 and score<=69:
    print(f"hello {name}, your grade is B")
elif score>=50 and score<=59:
    print(f"hello {name}, your grade is C")
elif score>=40 and score<=49:
    print(f"hello {name}, your grade is D")
elif score>=0 and score<=39:
    print(f"hello {name}, your grade is f")
else:
    print("you failed")
