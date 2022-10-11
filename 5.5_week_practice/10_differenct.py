set1 = {10, 20, 30}
set2 = {20, 40, 50}

for i in set2:
    if i in set1:
        set1.remove(i)

print(set1)