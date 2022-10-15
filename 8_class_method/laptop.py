class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self):
        self.age = self.age + 1

    def repair(self, age):
        self.repari_age = age

my_laptop = Laptop('ASUS', 1)
my_laptop.increase_age()

print(my_laptop.age)
my_laptop.repair(2)

print(my_laptop.__dict__)