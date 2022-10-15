savings = 0
while savings < 100:
    print("another new day")
    savings+=10
    print(f"savings balance is {savings} \n")

    while True:
        print("press 1 to play...and press 2 to end")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            fname = input("enter your fistname: ")
            Iname = input("enter your last name: ")
            print(f"your fullname is {fname} {Iname}")
        else:
            break