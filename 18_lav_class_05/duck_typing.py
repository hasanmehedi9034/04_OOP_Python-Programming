class School:
    def __init__(self, name):
        self.school_name = name
        
    def say_hello(self):
        print('say hello from school')

class Teacher:
    def __init__(self, name):
        self.teacher_name = name
        self.students = []
        
    def entry_student(self, studentObj):
        self.students.append(studentObj)
        
    def say_hello(self):
        print(f'Hello from teacher')
        
class Student(Teacher):
    def __init__(self, name):
        self.student_name = name
        Teacher.__init__(self, 'Rahim sir')
        Teacher.entry_student(self, self)
        
    def entry_in_a_teacher(self, teacherObj):
        teacherObj.students.append(self)
        
    def __repr__(self):
        return f'Student({self.student_name})'
    
# solaiman_mia = Teacher('Solaiman mia')
# rahim_mia =Teacher('Rahim mia')
# ms_rahim = Teacher('ms Rahim')    

# student = Student('Mehedi')
# student.entry_in_a_teacher(rahim_mia)
# student.entry_in_a_teacher(ms_rahim)

# print(rahim_mia.students)
# print(ms_rahim.students)

