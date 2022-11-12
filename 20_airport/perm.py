"""
a b c

a c b

b a c

b c a

c a b

c b a
"""

from itertools import permutations

# list = [1, 2, 3]
list = ['i', 'learn', 'python']

for i in permutations(list):
    print(i)

