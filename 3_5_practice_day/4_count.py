test_string = "P@#yn26at^&i5ve"

uppercase = 0
lowercase = 0
digits = 0
special_symbols = 0

for char in test_string:
    if (ord(char) >= ord('0')) and (ord(char) <= ord('9')):
        digits += 1
    elif (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
        lowercase += 1
    elif (ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
        uppercase += 1
    else:
        special_symbols += 1

print(f'Uppercase = {uppercase}\nLowercase = {lowercase}\nDigits = {digits}\nSymbol = {special_symbols}')