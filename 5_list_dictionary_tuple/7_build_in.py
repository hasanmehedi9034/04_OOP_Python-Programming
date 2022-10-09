actors_list = [
    {'name': 'salman', 'age': 23},
    {'name': 'kalman', 'age': 25},
    {'name': 'solaiman', 'age': 26},
    {'name': 'akmal', 'age': 20},
    {'name': 'sakib', 'age': 23}
]

sorted_actor = sorted(actors_list, key= lambda actor: actor['age'])
print(sorted_actor)