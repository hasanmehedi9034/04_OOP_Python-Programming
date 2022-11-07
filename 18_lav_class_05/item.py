import json

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def initialze(self):
        with open('extract.txt', 'r') as f:
            data = f.read()
            js = json.loads(data)
        
        for item in js:
            print(item)
            
item = Item(name ='test', price = 100)
item.initialze()