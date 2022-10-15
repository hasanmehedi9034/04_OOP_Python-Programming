class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class School:
    def __init__(self, name, teachers, courses, students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students

school_name = 'Phitron'
ds_course = Course('Data Structure', 'Einstein')
teacher_1 = Teacher('Einstein', ds_course)

algo_course = Course('Algo', 'Edison')
teacher_2 = Teacher('Edison', algo_course)

teachers = [teacher_1, teacher_2]
