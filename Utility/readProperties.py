import configparser

parser = configparser.ConfigParser()
parser.read(".\\Configuration\\config.ini")


class cnfParser:

    @staticmethod
    def getApplicationUrl():
        Url = parser.get('CommonInfo', 'url')
        return Url

    @staticmethod
    def getEmail():
        Email = parser.get('CommonInfo', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = parser.get('CommonInfo', 'password')
        return Password

    @staticmethod
    def getCountry():
        Country = parser.get('CommonInfo', 'country')
        return Country
