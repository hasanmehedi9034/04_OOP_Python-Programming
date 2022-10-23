class Student:
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks
    
    @property 
    def student_id(self):
        return self.__id
    
    @property
    def name(self):
        return self._name
    
    # @name.deleter
    # def name(self):
    #     del self._name
        
    
chowdury = Student('choto chowdury', 15, 55)
print(chowdury.student_id)
# chowdury.student_id = 77

# print(chowdury.student_id)

print(chowdury.name)

# del chowdury.name

print(chowdury.name)
print(dir(chowdury))

    
    