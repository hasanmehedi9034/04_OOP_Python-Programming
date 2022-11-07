class School:
    def __init__(self, name):
        self.school_name = name
        
    def __repr__(self):
        return f'School({self.school_name})'
    
class Teacher:
    def __init__(self, name):
        self.teacher_name = name
        
    def __repr__(self):
        return f'Teacher({self.name})'
    
class Student(Teacher, School):
    def __init__(self, teacher_name, school_name, name):
        # Teacher.__init__(self, teacher_name)
        # School.__init__(self, school_name)
        super().__init__(name)
        self.name = name
        
    def __repr__(self):
        return f'Student({self.name})'
    
student = Student('Rakib sir', 'trust shcool', 'Mehedi')
print(student.teacher_name, student.school_name)