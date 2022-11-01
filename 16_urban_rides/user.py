import hashlib
from brta import BRTA
from vehicles import CNG, Car, Bike
from ride_manager import uber
from random import randint

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
                
        with open('users.txt', 'a') as  file:
            file.write(f'{email} {pwd_encrypted}\n')
        file.close()
        print(self.name, 'user created')
        
    @staticmethod
    def log_in(email, password):
        strored_pass = ""
        
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if  email in line:
                    _, strored_pass = line.split(' ')
        file.close()
        
        hased_pass = hashlib.md5(password.encode()).hexdigest()
        
        if hased_pass == strored_pass:
            print('valid user')
            return True
        
        else:
            print('invalid user')
            return False
      
class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)
        
    def set_location(self, location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        pass
    
    def start_a_trip(self, fare):
        self.balance -= fare
        
class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry You failed, try again')
        else:
            self.license = result
            self.valid_driver = True
            
    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = CNG(vehicle_type, license_plate, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print("You are not a valid driver")
        
    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination
                  
rider1 = Rider('Rider 1', 'rider1@gmail.com', 'rider 1', randint(0, 100), 5000)
rider2 = Rider('Rider 2', 'rider2@gmail.com', 'rider 2', randint(0, 100), 5500)
rider3 = Rider('Rider 3', 'rider2@gmail.com', 'rider 3', randint(0, 100), 5500)

driver1 = Driver('driver 1', 'driver1@gmail.com', 'driver1', randint(0, 100), 5000)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 1234, 10)

driver2 = Driver('driver 2', 'driver1@gmail.com', 'driver2', randint(0, 100), 5000)
driver2.take_driving_test()
driver2.register_a_vehicle('car', 1234, 10)

driver3 = Driver('driver 3', 'driver1@gmail.com', 'driver3', randint(0, 100), 5000)
driver3.take_driving_test()
driver3.register_a_vehicle('car', 1234, 10)

driver4 = Driver('driver 4', 'driver1@gmail.com', 'driver4', randint(0, 100), 5000)
driver4.take_driving_test()
driver4.register_a_vehicle('car', 1234, 10)

print(uber.get_available_cars())
