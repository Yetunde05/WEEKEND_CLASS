for value in range(11):
    if value%2 == 0:
        print(value*3)
    elif  value%2 != 0:
        print(value*2)

le = [value*3 for value in range(11) if value%2 == 0]
print(le)
