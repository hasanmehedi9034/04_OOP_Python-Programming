from itertools import chain

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

def create_list(dict_):
    return list(chain.from_iterable((key, value) for key, value in dict_.items()))

output = create_list(d)
print(output)