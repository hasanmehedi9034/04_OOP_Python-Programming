class GroupChat:
    def __init__(self):
        self.__observers = []
        
    def  attach(self, observer):
        self.__observers.append(observer)
        
    def add_new_message(self, msg):
        self.notify(msg)
    
    def notify(self, msg):
        for observer in self.__observers:
            observer.update(msg)
            
class Observer:
    def __init__(self, name):
        self.name = name
        
    def update(self, msg):
        print(f'New Message for {self.name}: {msg}')
        
messenger = GroupChat()

abid = Observer('Abid')
navid = Observer('Navid')
sabid = Observer('Sabid')

messenger.attach(abid)
messenger.attach(navid)
messenger.attach(sabid)

messenger.add_new_message('Hey bro and sis')        
        
# go refactorguru and take some idea for design pattern       
