s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

def clean_string(text):
    return "".join([i for i in s if i.isalpha()])

output = clean_string(s)
print(output)