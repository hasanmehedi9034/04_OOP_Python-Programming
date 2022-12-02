'''
int, float, string, tuple, list, dictionary, set
'''

list1 = [1, 3, 4]

lst = [1, 3, 4, [5, 6, [7, 8, [9, 10, [11, 12]]]]]
lst[3][2][2][2].append(13)

# print(lst[3][2][2][2])

small_list = [1, 2, 3, 4]
# print(small_list[: : -1])



f = []
f.append('Mehedi')
f.append('Hasan')
print(f'First Name: {f[0]}\nLast Name: {f[1]}')