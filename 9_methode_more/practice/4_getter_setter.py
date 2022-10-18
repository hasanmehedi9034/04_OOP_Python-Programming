class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name

    @property
    def email(self):
        return f'{self.first.lower()}{self.last.lower()}@user.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, value):
        first, last = value.split(' ')

        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last

mark = User('mark', 'zuku')
print(mark.email)
print(mark.full_name)

mark.full_name = 'Mehedi hasan'
print(mark.full_name)
print(mark.email)
print(mark.first, mark.last)

# del mark.full_name
# print(mark.first)
