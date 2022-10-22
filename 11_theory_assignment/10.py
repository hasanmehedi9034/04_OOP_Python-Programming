import math

class Distance:
    def __init__(self, frist_point, second_point):
        self.frist_point = frist_point
        self.second_point = second_point
        
    def find_distance(self):
        # return math.sqrt( ((self.frist_point[0]-self.second_point[0])**2)+((self.frist_point[1]-self.second_point[1])**2))
        return math.dist(self.frist_point, self.second_point)
    
a = Distance([3, 3], [6, 12])

print(a.find_distance())