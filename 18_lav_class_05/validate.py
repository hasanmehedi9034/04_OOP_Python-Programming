class Item:
    def __init__(self, itemName, itemPrice):
        assert itemPrice >= 0, f'Error Line 3, {itemPrice} is Invalid'
        
        self.itemName = itemName
        self.itemPrice = itemPrice
        
class Person:
    def __init__(self, name, phone, age):
        assert age > 13, f"Only greater than 13 is accepted"
        assert len(phone) == 11, f'Invalid Phone no: {phone}'
        
        self.name = name
        self.phone = phone
        self.age = age
        
person = Person(name = 'Mehedi', phone = '2323', age = 100)
        
# item = Item('Plate', -10)
# print(item.itemName, item.itemPrice)