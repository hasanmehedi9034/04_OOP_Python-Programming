actors_list = [
    {'name': 'salman', 'age': 23},
    {'name': 'kalman', 'age': 25},
    {'name': 'solaiman', 'age': 26},
    {'name': 'akmal', 'age': 20},
    {'name': 'sakib', 'age': 23},
    {'name': 'sakib', 'age': 2}
]

actors_list = sorted(actors_list, key= lambda actor: actor['age'], reverse=False)

for i, value in enumerate(actors_list):
    for key, value in actors_list[i].items():
        print(f'{key} -> {value}')
    print()


