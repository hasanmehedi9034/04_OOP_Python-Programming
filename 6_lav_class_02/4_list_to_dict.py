my_list = ['@F1', 'OBCD', '@F2', 'ADDAB', '!', '@F3', 'OKKA', '!']

new_dict = dict(list(zip(my_list[0 : len(my_list) : 2], my_list[1 : len(my_list) : 2])))

print(new_dict)