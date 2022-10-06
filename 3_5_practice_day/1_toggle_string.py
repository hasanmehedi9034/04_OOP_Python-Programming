data = 'pHitrOn.iO presents "Python COuRSe"'
result_data = ""

for char in data:
    if (ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
        result_data += chr(ord('a') + ord(char) - ord('A'))
    elif (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
        result_data += chr(ord('A') + ord(char) - ord('a'))
    else:
        result_data += char

print(result_data)

