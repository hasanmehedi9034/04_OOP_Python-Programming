numbers= [10, 20, 10, 40, 50, 60, 70]
target= 50

def solution(numbers, target):
    for i, value in enumerate(numbers):
        
        if numbers[i] + numbers[i + 1] == target:
            return i + 1, i + 2

a, b = solution(numbers, target)
print(f'{a}, {b}')
