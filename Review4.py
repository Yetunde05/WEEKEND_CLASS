# TASK 1You are the principal of a school and you have been given the task to divide students into two groups based on their performance in percentage.
# Group 1: students who have a percentage of 80% and above (who will be awarded scholarship)
# Group 2: students who have score less than 30% (who will be evited from the college)
# the percentage of their performances is stored in a list below:
# performance = [90, 19, 89, 56, 89, 28, 87, 44, 94, 67, 21, 53, 12, 56, 67]
# Using filter functions, from the list above:
# i. create a new list called best_students that will hold all students that fall under group 1
# ii. create a new list called  low_students that will hold all students that fall under group 2
performance = [90, 19, 89, 56, 89, 28, 87, 44, 94, 67, 21, 53, 12, 56, 67]
best_students = filter(lambda x: x >= 80,performance)
print(list(best_students))
low_student = filter(lambda x: x<30,performance)
print(list(low_student))

# TASK 2
# You have completed 10 business deals this month. for each deal, your cut is 15% of the amount made.
# all deals are stored in a list called deals as shown below.
# deals = [102000, 12000, 5000, 9800, 15600, 17600, 43000, 89000, 90000, 78000]
# I.  create a newlist called my_cut that will hold your share of each deal (that's 15% of each deal)
# II. create a second list called company_cut that will hold the company's share of each deal(that's 85% of each deal)
# Hint: Use map functions
deals = [102000, 12000, 5000, 9800, 15600, 17600, 43000, 89000, 90000, 78000]
mycut =  map(lambda x: x*0.15,deals)
print(list(mycut))
company_cut = map(lambda x: x*0.85,deals)
print(list(company_cut))
