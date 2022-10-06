number = 76542

while(number > 0):
    digit = number % 10
    number = number // 10
    print(digit, end="")
