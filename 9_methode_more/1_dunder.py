# dunder
# magic / special method
# search dunder

class Person:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money

    def __call__(self):
        return f'This is {self.name} with age{self.age} have money'

    def __eq__(self, other):
        return self.age == other.age

    def __add__(self, other):
        # return self.money + other.money
        return self.age + other.age

alim = Person('Alim', 15, 400)
dalim = Person('Dalim', 16, 500)

# print(alim + dalim)
# print(alim())
# print(alim = dalim)
# x = 5
# print(type(alim))

print('Compare two object', )