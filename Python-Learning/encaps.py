# encapsulation
class company:
    def __init__(self):
        self.__companyName = "Google"  # private variable

    def companyName(self):
        print(self.__companyName)


c1 = company()
c1.companyName()
