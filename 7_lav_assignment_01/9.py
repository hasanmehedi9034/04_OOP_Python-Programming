replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

def replace_same_value(l, o, r):
    for i in range(len(l)):
        if o == l[i]:
            l[i] = r
    return l

def replace_word(string_):
    split_string = string_.split()

    for i in range(0, len(replace_with), 2):
        split_string = replace_same_value(split_string, replace_with[i], replace_with[i + 1])
    
    return "".join([" " + i for i in split_string])[1 : ]

output = replace_word(s)
print(output)