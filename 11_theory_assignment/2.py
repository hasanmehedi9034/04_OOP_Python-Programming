numbers = input().split('-')
numbers = list(map(lambda x : float(x), numbers))

def sum_of_array(numbers):
    return sum(numbers)

print(sum_of_array(numbers))