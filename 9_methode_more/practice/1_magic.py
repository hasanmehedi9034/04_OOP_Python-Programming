class Person:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money

    def __repr__(self):
        return f'Person({self.name})'

    def __mul__(self, p):
        if  type(p) is not int:
            raise  Exception('Invalid argument, must be int')

        self.name = (self.name + " ")  * p


p = Person('Mehedi', 23, 500)
p * 4
print(p)