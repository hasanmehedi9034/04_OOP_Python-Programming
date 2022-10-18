import math
import time

def timer(func):
    def inner(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        end = time.time()

        print(f'Total time taken: {round((end - start), 4)}')
    return inner

def Fibo(n):
    if (n == 1) or (n == 2):
        return 1
    return Fibo(n - 1) + Fibo(n - 2)

@timer
def get_factorial(n):
    result = math.factorial(n)

    print(f'Factorial of {n} is: {result}')

@timer
def get_fibo(n):
    result = math.fabs(n)
    print(f'Fibo {n} is: {Fibo(n)}')

