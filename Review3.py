# fruits = ['melon', 'apple', 'orange', 'mango']

# write a program to
# i.   ask a user for an input, then add the input value to the fruits list
# ii.  ask for a fruit item to be deleted from the fruits list
# iii. reverse the order of the fruits list
# iv.  sort the fruit
fruits = ['melon', 'apple', 'orange', 'mango']
New_fruit = input('Enter new fruit:')
fruits.append(New_fruit)
print(fruits)
out_fruit = input('fruit to be remove:')
fruits.remove(out_fruit)
print(fruits)
fruits.reverse()
fruits.sort()
print(fruits)
