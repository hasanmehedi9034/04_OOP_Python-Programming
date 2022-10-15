l = ["This", "is", "very", "fantastic"]

def create_string(list_):
    return "".join([" " + i for i in list_])[1 : ]

output = create_string(l)
print(output)