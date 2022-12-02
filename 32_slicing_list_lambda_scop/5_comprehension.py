# example: 1
lst = ['hello', 'world', 'python']
new_list = [i.upper() for i in lst]
# print(new_list)


#example: 2
x = 'hello'
# print(list(x))

# example: 3
lst = [x for x in range(1, 20) if x % 2 == 0]
# print(lst)

lst = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
# print(lst)

lst = ['Even' if x % 2 == 0 else 'Odd' for x in range(100)]
# print(lst)

lst = [(x, y) for x in [1, 2, 5, 6, 7] for y in [3, 4, 8, 9, 10] if x != y]
# print(lst)

dct = {f'{i}': i + 10 for i in range(10)}
# print(dct)

dct = {'jack': 30, 'rahim': 23, 'karim': 21, 'ripon': 50}
new_dct = {key:value for key, value in dct.items() if value % 2 == 0}
# print(new_dct)

new_dict = {key: ('Old' if value >= 50 else 'Young') for key, value in dct.items()}
# print(new_dict)

#last example
# dct = {k1 : {k2: k1 * k2} for k2 in range(6) for k1 in range(5)}
dct = {k1 : {n:n*n for n in range(2)} for k1 in range(10)}
print(dct)

