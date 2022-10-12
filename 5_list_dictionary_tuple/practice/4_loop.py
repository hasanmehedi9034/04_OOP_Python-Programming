numbers = [12, 45, 65, 23, 89, 78, 11]

marks = {
    'marks': 12,
    'chemistry': 45,
    'math': 56
}

for key, value in marks.items():
    print(f'{key} {value}')

print()

for i in marks:
    print(i, marks[i])

print()

for i, value in enumerate(numbers):
    print(i, value)