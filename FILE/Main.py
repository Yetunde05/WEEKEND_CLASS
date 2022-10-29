f = open("text.txt",'r+') 
# read the first 4 data
# print(f.read(4)) 
print(f.read())
f.write("The apple is green")
f.close()
