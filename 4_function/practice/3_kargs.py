def name(first_name, **names):
    try:
        print(first_name, middle_name, last_name)
    except NameError:
        print('args not  founded')

def names(**full_name):
    for key, value in full_name.items():
        print(f'{key} -> {value}')


names(first_name="Mehedi", last_name="Hasan", sur_name="Parvez")
