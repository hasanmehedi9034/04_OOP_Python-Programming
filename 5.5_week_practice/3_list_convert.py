list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

new_list = []

for i in range(len(list1)):
    # new_list.append(list1[i] + list2[i])
    new_list[len(new_list) : ] = [list1[i] + list2[i]]

print(new_list)
