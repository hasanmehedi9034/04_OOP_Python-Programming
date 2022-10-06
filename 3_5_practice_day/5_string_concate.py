s1 = "Abc"
s2 = "Xyz"
s3 = ""

i = 0
j = len(s2)

while(j != 0):
    s3 += s1[i]
    s3 += s2[j - 1]
    i += 1
    j -= 1

print(s3)