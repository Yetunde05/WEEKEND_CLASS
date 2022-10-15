  


my_fruits = ["mango" , "pawpaw" , "apple" , "banana"]
print(my_fruits[1])
my_fruits[3] = "coconut"
print(my_fruits)
names = ("lola" , "funke" , "seun" , "tolu")
names = list(names)
print(names) 
names[2] = "univelcity"
print(names)
person = {
    "name" : "yetunde" ,
    "hobbies" : ["dancing" , "singing" , "gaming"] ,
    "menu" : {
        "morning" : "fried rice and chicken" ,
        "afternoon" : "tea" ,
        "evening" : "semo and egusi"
    }
}
evening_meal = person["menu"]["evening"]
print(evening_meal)
print(person["hobbies"][2])
evening_menu = person["menu"]["evening"] = "beans"
print(evening_menu)  

