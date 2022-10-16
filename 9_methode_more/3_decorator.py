import math
import time

def timer(func):
    def inner(*args, **kargs):
        print('Start')
        start = time.time()
        func(*args, **kargs)
        print('Time end')
        end = time.time()

        print(f'total time {end - start}')
    return inner

@timer
def get_fact(n):
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_fact(n = 100)