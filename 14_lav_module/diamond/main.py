class A:
    def print_something(self):
        print('I am on a')

class B(A):
    def print_something(self):
        print('I am on b')

class C(A):
    def print_something(self):
        print('I am on c')

class D(B, C):
    def print_something(self):
        print('I am on d')
        
        
        
obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_something()
obj2.print_something()
obj3.print_something()
obj4.print_something()