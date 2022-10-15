# write a program that will save the names of students
# in a text file. option1 should be to add student and
# option2 to display all students saved in the text file
# the program should use while loop so the program runs repeatedly

while True:
    print('enter option 1 to add names')
    print('enter option 2 to display names')
    print('enter option 3 to empty the textfile')
    print('enter option 4 to end the program')
    choice = int(input('enter your choice:'))
    if choice == 1:
        file = open('student_name.txt', 'a')
        student_name = input('what is your name: ')
        student_name += '\n'
        file.write(student_name)
        file.close()
    elif choice == 2:
        file = open('student_name.txt', 'r')
        lines = file.readlines() 
        student_name = []
        for student in lines:
            student = student.rstrip()
            student_name.append(student)
        print(student_name)
        file.close()
    elif choice == 3:
        file = open('student_name.txt', 'w')
        file.write('')
        file.close
    elif choice == 4:
        break


    
    

