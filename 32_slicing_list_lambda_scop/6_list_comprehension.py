lst = [[j for j in range(3)] for i in range(4)]
# print(lst)

r, c = (5, 5)
# lst = [[0] * c] * r
lst = [[0 for i in range(5)] for i in range(5)]
# print(lst)

lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
new_lst = [val for sublist in lst for val in sublist]
# print(new_lst)

lst = [['hello', 'world'], ['mango', 'banana'], ['python', 'java']]
new_lst = [st for sublist in lst for st in sublist if len(st) > 5]
print(new_lst)













