s1 = "mehedi"
s2 = "hasanmehehasanmehedmehedi"

def is_match(string_one, string_two):
    test_variable = 0
    result = False

    for char in string_two:
        if char == string_one[0]:
            for i in range(len(string_one)):
                if (i + test_variable) > len(string_two) - 1:
                    return False
                elif (string_one[i] == string_two[i + test_variable]):
                    result = True
                else:
                    result = False
        test_variable += 1

    return result

print(is_match(s1, s2))