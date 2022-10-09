# def square(x):
#     return x * x

square = lambda x: x * x
add = lambda x, y: x + y

numbers = [12, 45, 65, 23, 89, 78, 11]
users = [
    {
        'name' :'sakib',
        'age': 343
    },
    {
        'name' :'mehedi',
        'age': 30
    },
    {
        'name' :'hasan',
        'age': 40
    }
]

double_numbers = map(lambda x: x * 2, numbers)
filter_numbers = filter(lambda num: num > 50, numbers)
senior_artists = filter(lambda actor: actor['age'] > 35, users)

print(numbers)
print(list(double_numbers))
print(list(filter_numbers))
print(list(senior_artists))