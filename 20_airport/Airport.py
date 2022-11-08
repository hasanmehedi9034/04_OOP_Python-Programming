class Airport:
    def __init__(self, code, name, city, country, lat, long, rate):
        self.code = code
        self.city = city
        self.name = name
        self.country = country
        self.lat = lat
        self.long = long
        self.rate = rate
        
    def __repr__(self):
        return f'Airport: {self.name} in: {self.country} lat: {self.lat} long: {self.long}'
    
    
    