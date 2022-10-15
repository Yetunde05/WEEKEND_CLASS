# perform the following:

# i. create a new file called assignment1.py
# ii. create a variable called amount and give it a string value
# iii. create  a variable called name and give it a string value
# iv. using string concatenation, print hello name, you have amount naira as your balance
Amount = "50"
name = 'olayinka'
print(f'hello {name}, you have {Amount} naira as your balance')

# v.  this is a list
#     fruits = ["mango", "orange", "pawpaw", "apple"]
# vi. print the first fruit in the fruits list
# vii print the last fruit in the fruits list
fruits = ["mango", "orange", "pawpaw", "apple"]
print(fruits[0])

# viii. this is a dictionary

student = {
        "esther":{
            "fullname": "esther iyi",
            "class": "300 level",
            "cgpa": 4.5,
            "courses_taken": {
                "maths": 50,
                "english": 70,
                "chemistry": 80,
            }
        },
        "ade":{
            "fullname": "ade james",
            "class": "200 level",
            "cgpa": 4.5,
            "courses_taken": {
                "maths": 90,
                "english": 100,
                "chemistry": 40,
            }
        }

    }


# ix. print ade's maths score
# x. print ade's CGPA
# xi. print esther's class

Ade_maths_score = student["ade"]['courses_taken']['maths']
print(Ade_maths_score)
Ade_cgdpa = student['ade']['cgpa']
print(Ade_cgdpa)
Esther_class = student['esther']['class']
print(Esther_class)