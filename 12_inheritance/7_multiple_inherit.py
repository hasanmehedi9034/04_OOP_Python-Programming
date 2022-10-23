class School:
    def __init__(self, school_name):
        self.school_name = school_name
        print('School init called')
        
class SportsTeam:
    def __init__(self, sport):
        self.sport = sport
    
class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print('Grade class init called')

class Student(School, Grade, SportsTeam):
    def __init__(self, name, grade_name, school_name, sport):
        self.name = name
        print('Student init called')
        Grade.__init__(self, grade_name)
        School.__init__(self, school_name)
        SportsTeam.__init__(self, sport)
        
        
ananta_j = Student('Ananta Jalil', 'MBA', 'UK School', 'India')

print(ananta_j.name)
print(ananta_j.grade_name)
print(ananta_j.school_name)
print(ananta_j.sport)
    
