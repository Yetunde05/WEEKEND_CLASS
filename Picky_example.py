import pickle


fruits = ['banana', 'mango', 'coconut']
file = open('pickletext.txt', 'wb')
pickle.dump(fruits,file)
file.close()

 
file = open('pickletext.txt', 'rb')
pickled_data = file.read()
print(pickled_data)
fruits_list = pickle.loads(pickled_data)
print(fruits_list)
print(type(fruits_list))  