class UserService:
    def __init__(self):
        self.__users = set()
    
    def register(self, username):
        if username in self.__users:
            return False
        self.__users.add(username)
        return True
    
    def authenticate(self, username):
        if username not in self.__users:
            return False
        return True