class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart[len(self.cart) : ] = [item]

shoper_1 = Shop('Mehedi')
shoper_1.add_to_cart('tshirt')
print(shoper_1.cart)