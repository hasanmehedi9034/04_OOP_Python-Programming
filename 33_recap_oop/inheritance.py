class GrandParent:
    def __init__(self):
        self.string = 'I am grand parent'

class Parent(GrandParent):
    def __init__(self):
        self.string1 = 'I am a parent'
        
class Child(Parent):
    def __init__(self):
        self.string2 = 'I am a child'
        # Parent.__init__(self)
        # super().__init__()
        Parent.__init__(self)
        GrandParent.__init__(self)
        
                
c = Child()
print(c.string)
print(c.string1)













