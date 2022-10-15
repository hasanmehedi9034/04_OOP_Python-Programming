class Calculator:
    def add(self, a, b):
        return a + b

    def  substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

my_calculator = Calculator()

print(my_calculator.add(2, 3))
print(my_calculator.substract(5, 2))
print(my_calculator.multiply(3, 3))
print(my_calculator.divide(10, 2))