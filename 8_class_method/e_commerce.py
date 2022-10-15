class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart[len(self.cart) : ] = [{'name': item, 'price': price, 'quantity': quantity}]

    def checkout(self, amount):
        price = 0

        for  item in self.cart:
            print(item)
            price += item['price'] *  item['quantity']
        
        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price:
            return f'take your back: {amount - price}'
        else:
            return f'here are the item'

shopping = Shopper('bag tan')
shopping.add_to_cart('shirt', 200, 2)
shopping.add_to_cart('shoe', 300, 1)
shopping.add_to_cart('pant', 500, 2)

shopping.checkout(5000)