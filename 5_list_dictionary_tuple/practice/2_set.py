numbers = [12, 45, 56, 45, 12]
set_numbers = set(numbers)


print(numbers)
print(set_numbers)


if 12 in set_numbers:
    set_numbers.remove(12)

print(set_numbers)