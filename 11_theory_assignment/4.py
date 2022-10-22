input_string = input()
# input_string = 'x3b4U5i2'

all_number = [i for i in input_string if i.isnumeric()]
all_char = [i for i in input_string if not i.isnumeric()]

targeted_dict = dict(zip(all_char, all_number))
targeted_dict = dict(sorted(targeted_dict.items(), key=lambda i: i[0].lower()))

for key, value in targeted_dict.items():
    for i in range(int(value)):
        print(key, end="")