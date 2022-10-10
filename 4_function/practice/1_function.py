def double_it(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    
    return numbers

def user_details():
    user = {
        'name': 'Mehedi',
        'age': 23
    }
    return user

numbers = [1, 2, 3, 4]
double_number = double_it(numbers=numbers)
user_detail = user_details()

print(numbers)
print(user_detail)
