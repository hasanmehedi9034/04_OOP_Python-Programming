from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    def  __init__(self):
        self.__name = 'monkey'
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @property
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def move(self):
        print('Moving around in the zoo')
    
class Monkey(Animal):
    def sing(self):
        print('Monkey is singing')
    
    def name(self):
        return self.__name
        
    def eat(self):
        print('Eating banana')
        
    def move(self):
        print('monkey in the walking at the zoo')
        super().move()
    
    @property()
    def name(self):
        return 'Monkey'
        
class Tiger(Animal):
    def eat(self):
        pass
    
    def move(self):
        pass
        
layka = Monkey()
print(layka.name)
layka.eat()
layka.move()