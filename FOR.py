for i in range(5):
    print(i)

fruit_list = ["pear", "mango", "banana", "pineapple"]
for i in fruit_list:
    print(f"{i} is really nice")

scores = [10, 45, 27, 89, 90, 90]
for score in scores:
    print(score*2)

for i, v in enumerate(fruit_list):
    print(f"{v} is at the index of {i}")

students = ["dominion", "yetunde", "justice"]


dict_students = {}
for student in students:
    mat_no  = input("enter matric number: ")
    location = input("enter your location: ")

    dict_students[student]={
        "matric_no" : mat_no,
        "location" :location
    }
    print(dict_students)