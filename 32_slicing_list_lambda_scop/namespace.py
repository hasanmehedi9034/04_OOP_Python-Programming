# namespace, scop
x = 5

# import index
# print(x)

# def f():
#     print("Hello Mehedi")


# LEGB
'''
    L = Local
    E = Enclosed
    G = Global
    B = build
'''


# Enclosed scope
s = "I am global"
def outer_scope():
    # s = "I am local"
    
    def inner_scope():
        # s = "I am enclosed"
        print(s)
    
    inner_scope()
outer_scope()

from math import pi
# pi = 9.33
# local global builtin enclosed
def outer_scope():
    pi = 9
    def inner_scope():
        pi = 5
        print(pi)
    inner_scope()
outer_scope()
print(pi)


# enclosed > local > global > builtin


