class Phone:
    manufactured = 'china'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self, number, text):
        sms = f'Sending: {text} to {number}'
        return sms

my_phone = Phone('samsung', 4300, 'mint blue')
# print(my_phone.send_sms('013', 'i missed to miss you'))
print(my_phone.brand)
print(my_phone.manufactured)