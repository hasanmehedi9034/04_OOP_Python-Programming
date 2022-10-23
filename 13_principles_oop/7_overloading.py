# print(max(12, 45, 78, 12, 98, 45, 20, -8))
# print(max([1, 2, 13, 14, 30]))
# print(max('a', 'p', 'k', 'c'))

def add(num1, num2, num3 = 0, num4 = 0):
    return num1 + num2 + num3 + num4

print(add(2, 3))
print(add(12, 13, 50))

def add2(*args):
    pass

# operator overloadin
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance
        
    def __add__(self, other):
        return self.__balance + other.__balance
        
    def __eq__(self, __o: object):
        return self.__balance == __o.__balance
    
my_account = Account('sakib al hasan', 50000)
her_account = Account('Shishir vabi', 90000)
result = my_account + her_account

print(result)

print(my_account == her_account)