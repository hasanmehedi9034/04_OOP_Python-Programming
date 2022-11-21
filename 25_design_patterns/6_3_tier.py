# google (design pattern vs architecture pattern)

class Data:
    def __init__(self):
        self.data = {
            'order1': {
                'item': 'laptop',
                'price': 45000
            },
            'order2': {
                'item': 'tablet',
                'price': 4000
            },
            'order3': {
                'item': 'watch',
                'price': 2500
            },
            'order4': {
                'item': 'phone',
                'price': 50000
            }
        }
        
    def get_order_detail(self, orderId):
        return self.data[orderId]   
    
class Application:
    pass

class GUI:
    pass

     