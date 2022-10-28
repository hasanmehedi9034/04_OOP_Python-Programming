""" All about mankind """

class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, gender, height, weight, cases, nationality):
        super().__init__(gender, height, weight)
        
        self.cases = cases
        self.nationality = nationality
        
class CsEngineer(Human):
    def __init__(self, love_to_code: bool, has_gf: bool, gender: str, height: int, weight: int):
        super().__init__(gender, height, weight)
        
        self.love_to_code = love_to_code
        self.has_gf = has_gf
        
if __name__ == '__main__':
    police = Police(gender= 'male', height=  '5 feet', weight= '20kg', cases='No', nationality='Bangladeshi')
    print(police.height)

    eng = CsEngineer(True, False, 'male', 84, 50)
    print(eng.height)

    eng2 = CsEngineer(has_gf = 'True', love_to_code = True, gender = 'male', height = 32, weight =30)
    print(eng2.has_gf)