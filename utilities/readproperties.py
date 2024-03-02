import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\girish kadam\\Desktop\\Binder\\Configuration\\config.ini")


class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('user info', 'loginUrl')
        return LoginUrl


    @staticmethod
    def getEmail():
        Email = config.get('user info', 'User_email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('user info', 'Password')
        return Password
