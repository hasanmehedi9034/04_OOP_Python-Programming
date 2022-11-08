a=input('word-1: ')
b=input('word-2: ')

def nearly_equal(a,b):
    str1 = 0
    str2 = 0
    ans = 0
    while(str1 < len(a) and str2 < len(b)):
        if(a[str1] != b[str2]):
            ans += 1
            if(len(a) > len(b)):
                str1 += 1
            else:
                str1 -= 1
        if(ans > 1): 
            return False
        str1 = str1 + 1
        str2 = str2 + 1
    if( ans < 2):
            return True
 
output=nearly_equal(a, b)
print(output)