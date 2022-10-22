a, n = input().split()
a = int(a)
n = int(n)

def exp(a, n):
    ans = 1
    for i in range(n):
        ans *= a
    return ans

print(exp(a, n))