def add(number1, number2):
    total = number1 + number2
    return total

def multiply(*numbers):
    result = 0
    for num in numbers:
        print(num)

def add(num1, *numbers):
    print(numbers, end=" ")

add(1, 2, 3, 4, 5)

# print(add(12, 24))
# print(add(number2=20, number1=10))

# multiply(1, 2, 3, 4, 5)