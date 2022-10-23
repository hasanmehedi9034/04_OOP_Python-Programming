class Account:
    def __init__(self, holder):
        self.account_holder = holder

class StudentAccount(Account):
    def __init__(self, holder, balance, school):
        self.__balance = balance
        
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'No money for you'
        else:
            self.__balance -= amount
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
nas = StudentAccount('Nas Daily', 12000, 'Nas Academy')

print(nas.get_balance())
print(nas._StudentAccount__balance)
    