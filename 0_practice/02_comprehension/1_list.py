bits = [True, False, True, False, True, False, True, False, True, False]
converted_bits = [1 if b == True else 0 for b in bits]

fruits = ['apples', 'bananas', 'strawberries']
fruits = [value.upper() for i, value in enumerate(fruits)]

my_string = "HelloMyNameIsMariys"

my_string = "".join(
    [i if i.islower() 
    else (" " + i.lower()) if i in ['N', 'I']
    else (" " + i) 
    for i in my_string]
    )[1 : ]

print(my_string)

new_string = ""
for i in my_string:
    if i.islower():
        new_string += i
    elif i in ['I', 'N']:
        new_string += " " + i.lower()
    else:
        new_string += " " + i

new_string = new_string[1 : ]
print(new_string)
