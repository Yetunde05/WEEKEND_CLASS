menu = {
    "morning": "Bread and Tea",
    "post-morning": "Ginger Tea" ,
    "afternoon": "Rice and egg" ,
    "evening": "Spaghetti"
}
menu.get("morning")
print(menu["morning"])
dinner_type = input("what meal do you want to eat:")
meal = menu.get(dinner_type)
if meal == None:
    print(f"we dont have a meal for(dinner_type) time")
else:
 print(f"your (dinner_type) meal is meal")

 def greeting(name):
    print(f"hello {name}")
    greeting("yetunde")