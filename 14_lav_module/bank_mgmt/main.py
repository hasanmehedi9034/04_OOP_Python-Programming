"""Manages Bank Account"""


class Account:
    acc_id = 1
    
    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance
        
        # update account id
        self.account_id = Account.acc_id
        Account.acc_id += 1
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
        
acc_1 = Account('Mehedi', 23, 95323, 500)
acc_2 = Account('Hasan', 24, 95323, 40)

# print(acc_1.account_id)
# print(acc_2.account_id)

acc_1.deposit(300)
acc_1.withdraw(100)

print(acc_1.balance)