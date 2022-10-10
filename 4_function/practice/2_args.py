def multiply(number1, *numbers):
    if 5 in numbers:
        return True
    else:
        return False

multiply(1, 2, 3, 4, 5)

print(multiply(1, 2, 3, 5, 6))
