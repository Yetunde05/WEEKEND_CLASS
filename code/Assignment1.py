amount = "20"
name = "yetunde"
print("hello "  +    name   +    " you have "     +   amount   +   " naira as your balance")

fruits = ["mango", "orange", "pawpaw", "apple"]
fruit1 = fruits[0]
print(fruit1)
lastfruit = fruits[-1]
print(lastfruit)
student = {
    "esther" : {
        "fullname" : "esther iyi" ,
        "class" :  "300 level" ,
        "cgpa" : 4.5 ,
        "courses_taken" : {
            "maths" : 50 ,
            "english" : 70 ,
            "chemistry" : 80 ,

        }
    } ,

    "ade" : {
        "fullname" : "ade james" ,
        "class" :  "200 level" ,
        "cgpa" : 4.5 ,
        "courses_taken" : {
            "maths" : 90 ,
            "english" : 100,
            "chemistry" : 40 ,

        }
    }
}
ademaths = student["ade"]["courses_taken"]["maths"]
print(ademaths)
ade_cgpa = student["ade"]["cgpa"]
print(ade_cgpa)
esther_class = student["esther"]["class"]
print(esther_class)