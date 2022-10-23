class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder # public attribute
        self.__balance = initial_balance # private attribute
        self._account_number = 165
        
    def deposit(self, amount):
        print(f'Adding {amount} to your account')
        self.__balance += amount
        
    def withdraw(self, amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -= amount
    
class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school):
        self.school = school
        super().__init__(holder, initial_balance)
        
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self._account_number
    
    
rafsan = StudentAccount('Rafsan', 50000, 'IUB')

rafsan.deposit(2000)
rafsan.deposit(35000)
rafsan.deposit(15000)

print(rafsan._account_number)




