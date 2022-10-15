s = "I,have,been,practising,python,since,the,course,started"

def replace_comma_with_space(text):
    return "".join([i if i.isalpha() else " " for i in text])

output = replace_comma_with_space(s)
print(output)