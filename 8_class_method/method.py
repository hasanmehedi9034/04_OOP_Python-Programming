def add (a, b):
    return a + b

def deduct(a, y):
    return a - y



class Phone:
    color = 'Black'
    features = ['camera', 'water proof', 'can be used as a hammer']

    def call(self):
        print('ring ring ring')

    def send_sms(self, number, text):
        sms = f'sending {text} to {number}'
        return sms

my_phone = Phone()
my_phone.call()
print(my_phone.send_sms('013', 'i missed to miss you'))