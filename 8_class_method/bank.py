class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.min_withdraw:
            return f'no money for you. Min withdraw: {self.min_withdraw}'

        elif withdraw_amount > self.max_withdraw:
            return f'you crossed  daily limit: {self.max_withdraw}'

        elif withdraw_amount > self.balance:
            return 'You are broke!! No money for you'

        else:
            self.balance -= withdraw_amount
            return f'Here is your money: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return f'Your balance is: {self.get_balance()}'

my_bank = Bank(8000)

print(my_bank.deposit(100))
        