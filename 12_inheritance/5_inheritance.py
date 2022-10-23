# base class
class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        
    def re_sale(self):
        print('Ready to sell again')

class Laptop(Device):
    def __init__(self, brand, price, color, disc_size):
        super().__init__(brand, price, color)
        
        self.disc_size = disc_size
        
    def run(self):
        print(f'Running the laptop')
        
    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price
        
    def __repr__(self):
        return f'Laptop {self.brand}: {self.price}: {self.color}'


class Phone:
    def __init__(self, brand, price, color, camera, sim_number):
        self.brand = brand
        self.price = price
        self.camera = camera
        self.color = color
        self.sim_number = sim_number
    
    def is_dual_sim(self):
        return self.sim_number > 1
    
    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price
        
    def __repr__(self):
        return f'Phone {self.brand}: {self.price}: {self.color}'
        
        
class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
    
    def is_digital(self):
        return self.watch_type == 'digital'
    
    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price
    
    
class Manager:
    def __init__(self, name, salary, experience, designation):
        pass
    
    def day_total_sales(self):
        pass
    
    def handle_customer_complain(self):
        pass
    
    def withdraw_salary(self):
        pass
    
    
class SalesPerson:
    def __init__(self, name, salary, experience, designation, commission):
        pass
    
    def handle_customer(self):
        pass
    
    def withdraw_salary(self):
        pass
    

lenovo = Laptop('Lenovo', 42000, 'Black', '500GB')
hp = Laptop('HP', 35000, 'Silver', '250gb')

print(lenovo)
print(hp)

print()

oppo = Phone('OPPO', 15000, 'black', '15mp', 2)
samsung = Phone('samsung', 21000, 'blue', '20mp', 2)
print(samsung)
print(oppo)

hp.re_sale()
print(hp.brand)