data = "aNtEriOur\n\t>>"

new_data = data.lower()

output_data = ""

for char in new_data:
    # print(char)
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        output_data += char + "_"

output_data = output_data.rstrip(output_data[-1])

print(output_data)
