def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

def long_name(**kargs):
    print(kargs)

def name_mixed(first, last, **name_parse):
    print(first, last, name_parse)

def all_types(first, *args, **kargs):
    print(first)
    print(args)
    print(kargs)

    for key, value in kargs.items():
        print(f'key: {key}, value: {value}')

all_types("abd", 'ddd', 'kjk','lll', 'pp', name="Mehedi")
