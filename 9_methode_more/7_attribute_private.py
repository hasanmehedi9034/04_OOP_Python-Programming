class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.__phone = phone

    def get_password(self):
        return self.__password

    def user_login(self, name, password):
        if name ==  self.name and password == self.__password:
            return True
        return False

ryan = User('Ryan Dal', 'NODEABCE', '076305032')

# print(ryan.__password)
# print(ryan.__phone)
print(ryan.get_password())

print(ryan.user_login('Ryan Dal', 'NODSEABCE'))