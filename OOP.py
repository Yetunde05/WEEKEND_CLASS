class car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def get_brand(self):
        return self.brand
    def get_price(self):
        return self.price
c1 = car("Tundra", 8358000)
print(c1.get_brand())
print(c1.get_price())
# class car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#     def get_brand(self):
#         return self.brand
# c1 = car("Tundra", 8358000)
# print(c1.get_brand())
        