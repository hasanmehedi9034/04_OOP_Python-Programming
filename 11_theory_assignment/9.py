class A:
    def __init__(self, x, n):
        self.X = x
        self.n = n
        
    def sum(self):
        return self.X + self.n
    def pow(self):
        return pow(self.X, self.n)
    
a = A(2, 3)

print(a.sum(), a.pow())