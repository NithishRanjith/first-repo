class laptop:
    def __init__(self):  # constructor
        print("demo")
        self.price = 0
        self.ram = ""

    def display(self):  # self - current object ---> display(hp)
        print("display")
        print("RAM", self.ram)
        print("Price", self.price)


hp = laptop()
hp.price = 25
hp.ram = "6GB"
hp.display()  # ---> hp.display(hp)

# self - current object
