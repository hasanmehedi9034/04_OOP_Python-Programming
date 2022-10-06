data = "firebaby"

data = 'firebaby'
shift = 4
output = ""

final_output = ""

for char in data:
    output += chr((ord(char) + shift - 97) % 26 + 97)

for ch in output:
    final_output += char(ord(ch) - shift) 

print(output)
print(final_output)