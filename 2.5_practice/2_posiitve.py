def make_positive(number):
    if(number < 0):
        return ((-1) * number)
    return number

number = make_positive(int(input())) 
print(number)