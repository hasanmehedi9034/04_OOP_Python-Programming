numbers = [12, 45, 65, 23, 89, 78, 11]
total = sum(numbers)

for i in numbers:
    print(i, end=", ")

print()

nums = {12, 45, 65, 23, 89, 78, 11}
for num in nums:
    print(num, end=" ")

print()

marks = {
    'marks': 12,
    'chemistry': 45,
    'math': 56
}

for key, value in marks.items():
    print(f'key: {key}, value: {value}')

for mark in marks:
    print(marks[mark])

for i, num in enumerate(numbers):
    print(i, num)