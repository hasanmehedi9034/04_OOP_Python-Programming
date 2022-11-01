class RideManager:
    def __init__(self):
        print("Ride manager activated")
        self.__available_cars = []
        self.__available_cng = []
        self.__available_bikes = []
        
    def find_a_vehicle(self):
        pass
    
    def get_available_cars(self):
        return self.__available_cars
    
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)
            
uber = RideManager()