item_power = lambda x,y: x**y

deals = [1000,3000,6000,2000]
my_share = map(lambda x: x *0.25, deals)
print(list(my_share))

scores = [100, 70, 20, 40, 20, 90, 70, 54, 89]
A_list = filter(lambda x: x>=70, scores)
print(list(A_list))

nums = range(1,8,2)
print(list(nums))

import time
print("code started")
print("waiting for 10 seconds.....")

time.sleep(10)
print("10 secs completed")

