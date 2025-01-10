class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return self.__password

    def check_password(self, password):
        return self.__password == password


UserAccount = UserAccount('lyaguha', 'hellrey_yt@bk.ru', 123)
UserAccount.set_password(321)
print(UserAccount.check_password('321'))
