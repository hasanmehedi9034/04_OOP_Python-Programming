nums = [1, 2, 3]
string = ['one', 'two', 'three']


new_object = zip(nums, string)
# print(list(new_object))

names = ['rahim', 'karim', 'halim']
salaries = [10, 20, 15]
new_obj = {name:salary for name, salary in zip(names, salaries)}
# print(new_obj)

n, s = zip(*new_object)
print(n, s)









