
while True:
    print('enter 1 to add fruit')
    print('enter 2 to display all fruits')
    print('enter anything else to break')
    choice = int(input('enter your choice: '))
    if choice == 1:
        file = open('fruits.txt', 'a')
        fruit_name = input('what is the fruit name: ')
        fruit_name += '\n'
        file.write(fruit_name)
        file.close()
    elif choice == 2:
        file = open('fruits.txt', 'r')
        lines = file.readlines()
        fruits_list = []
        for fruit in lines:
          fruit = fruit.rstrip()
          fruits_list.append(fruit)
        print(fruits_list)
        file.close()
    else:
        break

    
    

    

    
