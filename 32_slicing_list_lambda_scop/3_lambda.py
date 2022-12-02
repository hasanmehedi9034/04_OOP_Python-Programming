def greet():
    print('Good Morning')

'''
a = lambda arg: expression
'''

a = lambda : print('Hello Good Morning')

s = 'Phitron'
new_s = lambda st: print(st.upper()[: : -1])

mx = lambda a, b: a if(a > b) else b

lst = [1, 2, 3]
new_lst = [lambda arg = i: arg * 2 for i in lst]
# print(new_lst)

my_list = [1, 2, 3, 4, 5, 6, 7]
new_lst = list(filter(lambda x: (x % 2 == 0), my_list))
# print(new_lst)

string_list = ['hello', 'world', 'python']
new_s = list(map(lambda x : x.upper(), string_list))
# print(new_s)

from functools import reduce
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, lst)
# print(sum)




print_greetings = lambda : (print("Hello", end=" "), print("Mehedi", end=" "))
print_greetings()



