import time
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

start = time.time()

for i in range(500):
    print(i, fib(i))

end = time.time()

mili_sec = end - start
print(f'Time took: {end - start}')