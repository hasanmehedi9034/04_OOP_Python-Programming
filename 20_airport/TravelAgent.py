from All_Airports import AllAirports
from Air_lines import AirLines

class TravelAgent:
    def __init__(self, name):
        self.name = name
        self.trips = None
        self.all_airports = AllAirports()
        self.air_lines = AirLines()
    
    '''
        params: 
        start: starting city code 
        end: destination
        start date:  date when you want to start trip
        
        return: 
        aircraft, price/cost
        
        notes: use airline to select aircraft
    '''
    def set_trip_one_city_one_way(self, start, end, start_date):
        price = self.all_airports.get_ticket_price(start, end)
        distance = self.all_airports.distance_between_two_airports(start, end)
        aircraft = self.air_lines.get_aircraft(distance)
        
        return [aircraft, price]
    
    def set_trip_one_city_two_way(self):
        pass
    
    def set_trip_multi_city_one_way(self):
        pass
    
    def set_multi_city_round(self):
        pass
    
    def __repr__(self):
        return f'TravelAgent: {self.name}'  
    