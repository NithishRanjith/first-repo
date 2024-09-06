class laptop:
    chargerType = "C-Type"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setPrice(self, price):  # instance method
        self.price = price

    def getPrice(self):  # instance method
        print(self.price)

    @classmethod  # decorators
    def setCharger(cls):
        cls.chargerType = "B-Type"
        print(cls.chargerType)

    @staticmethod
    def info():  # static method
        print("This is laptop class")


hp = laptop()
hp.setPrice(23)
hp.getPrice()
laptop.setCharger()
hp.info()
