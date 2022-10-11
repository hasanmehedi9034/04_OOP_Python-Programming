sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
values = [sample_dict[v] for v in keys]

new_dictionary = dict(list(zip(keys, values)))

print(new_dictionary)