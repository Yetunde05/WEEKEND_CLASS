students = ["dominion", "yetunde", "justice"]
for index, student_name in  enumerate(students):
    print(f"current student is {student_name}")
    last_name = input("enter your last name: ")
    full_name = f"{last_name} {student_name}"
    students[index] = full_name
    print(students)

    fruits = ["apple", "mango", "apple", "coconut"]
    print(list(enumerate(fruits))) 
