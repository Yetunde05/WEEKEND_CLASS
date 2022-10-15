fav_list = []
while True:
    print("Enter 1 to add a new fruit\nEnter 2 or anything else to terminate")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        fruit_name = input("Enter fruit: ")
        fav_list.append(fruit_name)
        print(f"{fruit_name} has been added to the list")
    elif choice == 2:
        fruit_name = input("Enter fruit: ")
        fav_list.remove(fruit_name)
        print(f"{fruit_name} has been removed from the list")
        print(fav_list)
    else:
        print(fav_list)
        break