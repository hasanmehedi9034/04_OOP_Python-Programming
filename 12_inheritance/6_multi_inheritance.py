class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license
        self.price = price
    
    def start(self):
        print(f'{self.name} started')
        
class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.available_seat = seat
        self.ticket_price = ticket_price
        
    def sell_ticket(self, quantity, ticket_price, amount, customer_name):
        self.available_seat -= quantity
        remainer = amount - (self.ticket_price * quantity)
        
        if remainer >= 0:
            return Ticket(customer_name)
        return 'No ticket for you'
    
class ACBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price):
        pass
    
class MiniBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price):
        pass
    

class Ticket:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        
        