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

double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers)


square = lambda x: x * x
add = lambda x, y: x + y

# print(square(2))
# print(add(10, 2))