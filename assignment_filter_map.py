performance = [90, 19, 89, 56, 89, 28, 87, 44, 94, 67, 21, 53, 12, 56, 67]
best_student = filter(lambda x: x>=80, performance)
names = ["racheal", "funke", "tolu", "seun", "tope"]
output = zip(names,best_student)
group1 = list(output)
print(group1)

low_student = filter(lambda x: x<30, performance)
low_names = ["shade", "lola" , "funsho" , "tobi"]
semi_output = zip(low_names,low_student)
group2 = list(semi_output)
print(group2)

deals = [102000, 12000, 5000, 9800, 15600, 17600, 43000, 89000, 90000, 78000]
my_cut = map(lambda x: x*0.15, deals)
print(list(my_cut))

company_cut = map(lambda x: x*0.85, deals)
print(list(company_cut))



performance = [90, 19, 89, 56, 89, 28, 87, 44, 94, 67, 21, 53, 12, 56, 67]
best_student = filter(lambda x: x>=80, performance)
group1 = list(best_student)
print(group1)