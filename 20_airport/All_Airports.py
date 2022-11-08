from math import radians, sin, cos, atan2, sqrt
import csv
from  Airport import Airport

class AllAirports:
    def __init__(self):
        self.airports = None
        self.load_airport_data('./data/airport.csv')
    
    def load_airport_data(self, file_path):
        airports = {}
        currentcy_rates = {}
        country_currency = {}
        
        # get currency name <---> rate
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currentcy_rates[line[1]] = line[2]
        file.close()
        
        # dictionary country <-------> currency name
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()
        
        with open(file_path, 'r', encoding='utf8') as file:
            lines = csv.reader(file)
            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currentcy_rates[currency]
                    airports[line[4]] = Airport(line[4], line[1], line[2], line[3], line[6], line[7], rate)
            except KeyError as e:
                print(e)
            self.airports = airports
        file.close()
        
        # print(currentcy_rates)
        # print(country_currency)
            
        # for airport in self.airports.items():
        #     print(airport)
        
    def get_distance_betweet_two_airports(self, lat1, long1, lat2, long2):
        radius = 6371
        
        lat_diff = radians(lat1 - lat2)
        lon_diff = radians(long1 - long2)
        
        arc = (sin(lat_diff / 2) * sin(lat_diff / 2) + 
               cos(radians(lat1)) *  cos(radians(lat2)) * 
               sin(lon_diff / 2) * sin(lon_diff / 2))
        c = 2 * atan2(sqrt(arc), sqrt(1 - arc))
        distance = radius * c
        
        return distance
        
AllAirports()