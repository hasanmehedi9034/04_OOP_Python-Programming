def swap(a, b):
    a, b = b, a
    return a, b

def print_format(a):
    for i in range(len(a)):
        if i != 0:
            a[i], a[i - 1] = swap(a[i], a[i - 1])
        for j in a:
            print(j, end='')
        print()

total_element = int(input('type a number: '))
a = [i for i in range(1, total_element + 1)]
    
print_format(a)

