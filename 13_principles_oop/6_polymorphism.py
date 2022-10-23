class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        print('animal making some sound')
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print('meow meow')
        
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        
    def make_sound(self):
        print('Bark Bark')
        
class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print('ney ney')
        
     
don = Cat('don')

shepard = Dog('German Shepard')

don2 = Dog('Asol don')

manik = Horse('Manik Roton')

animals = [don, shepard, manik, don2]
for animal in animals:
    animal.make_sound()
    