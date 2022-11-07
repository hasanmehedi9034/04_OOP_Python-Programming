class Item:
    all = []
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
        self.all.append(self)
        
    def __repr__(self):
        return f'{self.item_name}-{self.item_price}'
        
item1 = Item(item_name = 'Bowl', item_price = 150)
item2 = Item(item_name = 'Plate', item_price = 100)
item1.discount = 10
item2.offer = '60%'

print(Item.all)
 
Item.all.append(item1)

print(item1.__dict__)
print(item2.__dict__)

print(Item.all)