numbers = [13, 23, 45, 35, 23, 30]
names = ['sakib', 'sabbir', 'salman']
ages = [10, 20, 30]

odd_numbers = []
for num in numbers:
    if  num % 2 != 0:
        odd_numbers.append(num)

# print(odd_numbers)

odd_numbers2 = [num for num in numbers if num % 2 != 2 and num % 5 == 0]
print(odd_numbers2)

pairs = [(name, age) for name in names for age in ages if age >= 30]
print(pairs)