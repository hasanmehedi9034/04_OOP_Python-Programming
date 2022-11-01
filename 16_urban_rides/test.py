import linecache

riders_email = []
total_lines = 0

with open('users.txt', 'r') as  f:
    total_lines = len(f.readlines())
f.close()

for i in range(total_lines):
    x = linecache.getline(r"users.txt", i + 1).strip()
    email, password = x.split(" ")
    riders_email.append(email)

# print(total_lines)

print(riders_email)